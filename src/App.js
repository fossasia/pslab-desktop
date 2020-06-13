import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { HashRouter, Route, Switch } from 'react-router-dom';
import { Snackbar } from '@material-ui/core';
import { MuiThemeProvider } from '@material-ui/core/styles';
import { ThemeProvider } from 'styled-components';
import Appshell from './components/Appshell';
import Home from './screen/Home';
import Oscilloscope from './screen/Oscilloscope';
import LogicAnalyzer from './screen/LogicAnalyzer';
import PowerSource from './screen/PowerSource';
import WaveGenerator from './screen/WaveGenerator';
import Multimeter from './screen/Multimeter';
import Sensors from './screen/Sensors';
import RobotArm from './screen/RobotArm';
import Settings from './screen/Settings';
import FAQ from './screen/FAQ';
import AboutUs from './screen/AboutUs';
import LoggedData from './screen/LoggedData';
import FrontLayout from './screen/Layout/FrontLayout';
import BackLayout from './screen/Layout/BackLayout';
import CustomDialog from './components/CustomDialog';
import DeviceScreen from './screen/DeviceScreen';
import theme from './theme';
import {
  openSnackbar,
  closeSnackbar,
  deviceConnected,
  deviceDisconnected,
  closeDialog,
} from './redux/actions/app';
import debounce from 'lodash/debounce';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class App extends Component {
  constructor(props) {
    super(props);
    this.deviceStatus = false;
    this.reconnect = false;

    this.state = {
      isReading: false,
      isWriting: false,
    };
  }

  startRead = debounce(command => {
    const { isReading } = this.state;
    const { device } = this.props;
    const { isConnected } = device;
    if (isConnected) {
      this.setState({
        isReading: true,
      });
      !isReading &&
        loadBalancer.sendData(ipcRenderer, 'linker', {
          command,
        });
    }
  }, 1000);

  stopRead = command => {
    const { isReading } = this.state;
    const { device } = this.props;
    const { isConnected } = device;
    if (isConnected) {
      isReading &&
        loadBalancer.sendData(ipcRenderer, 'linker', {
          command,
        });
    }
    this.setState({
      isReading: false,
    });
  };

  startWriting = debounce(deviceType => {
    const { isWriting } = this.state;
    const { device, dataPath } = this.props;
    const { isConnected } = device;
    if (isConnected) {
      this.setState({
        isWriting: true,
      });
      isConnected &&
        !isWriting &&
        loadBalancer.sendData(ipcRenderer, 'linker', {
          command: 'START_WRITE',
          deviceType,
          dataPath,
        });
    }
  }, 300);

  stopWriting = debounce(() => {
    const { isWriting } = this.state;
    const { device } = this.props;
    const { isConnected } = device;
    if (isConnected) {
      isWriting &&
        loadBalancer.sendData(ipcRenderer, 'linker', {
          command: 'STOP_WRITE',
        });
    }
    this.setState({
      isWriting: false,
    });
  }, 300);

  componentDidMount() {
    const { deviceConnected, deviceDisconnected } = this.props;

    ipcRenderer.on('DATA_WRITING_STATUS', (event, args) => {
      const { openSnackbar } = this.props;
      const { message } = args;
      openSnackbar({ message });
    });

    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected, message, deviceName, portName } = args;

      if (this.deviceStatus !== isConnected) {
        isConnected
          ? deviceConnected({
              deviceInformation: {
                deviceName: deviceName && deviceName.split("'")[1],
                portName,
              },
            })
          : deviceDisconnected();
        this.deviceStatus = isConnected;
      }

      this.startReconectLoop(isConnected, message);
    });
    loadBalancer.start(ipcRenderer, 'linker');
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('DATA_WRITING_STATUS');
    ipcRenderer.removeAllListeners('CONNECTION_STATUS');
    loadBalancer.stop(ipcRenderer, 'linker');
  }

  startReconectLoop = (isConnected, message) => {
    const { openSnackbar } = this.props;
    if (!isConnected) {
      loadBalancer.stop(ipcRenderer, 'linker');
      if (!this.reconnect) {
        openSnackbar({ message });
        this.reconnect = setInterval(() => {
          loadBalancer.start(ipcRenderer, 'linker');
        }, 2500);
      }
    } else {
      openSnackbar({ message });
      clearInterval(this.reconnect);
      this.reconnect = false;
    }
  };

  reset = () => {
    const { deviceDisconnected } = this.props;
    if (this.deviceStatus) {
      this.deviceStatus = false;
      deviceDisconnected();
      this.startReconectLoop(false, 'Device reset');
    }
  };

  render() {
    const {
      closeSnackbar,
      snackbar,
      dialog,
      closeDialog,
      dataPath,
    } = this.props;
    const { isReading, isWriting } = this.state;

    return (
      <MuiThemeProvider theme={theme}>
        <ThemeProvider theme={theme.pallet}>
          <HashRouter>
            <Appshell
              reset={this.reset}
              dataPath={dataPath}
              isWriting={isWriting}
              startWriting={this.startWriting}
              stopWriting={this.stopWriting}
            >
              <Switch>
                <Route path="/" exact component={Home} />
                <Route
                  path="/oscilloscope"
                  render={props => (
                    <Oscilloscope
                      {...props}
                      dataPath={dataPath}
                      isReading={isReading}
                      startRead={this.startRead}
                      stopRead={this.stopRead}
                      stopWriting={this.stopWriting}
                    />
                  )}
                />
                <Route
                  path="/logicanalyzer"
                  render={props => (
                    <LogicAnalyzer {...props} dataPath={dataPath} />
                  )}
                />
                <Route
                  path="/powersource/:filePath?"
                  render={props => (
                    <PowerSource {...props} dataPath={dataPath} />
                  )}
                />
                <Route
                  path="/wavegenerator/:filePath?"
                  render={props => (
                    <WaveGenerator {...props} dataPath={dataPath} />
                  )}
                />
                <Route
                  path="/multimeter"
                  render={props => (
                    <Multimeter
                      {...props}
                      dataPath={dataPath}
                      isReading={isReading}
                      startRead={this.startRead}
                      stopRead={this.stopRead}
                      stopWriting={this.stopWriting}
                    />
                  )}
                />
                <Route
                  path="/robotarm"
                  render={props => <RobotArm {...props} dataPath={dataPath} />}
                />
                <Route
                  path="/sensors"
                  render={props => <Sensors {...props} />}
                />
                <Route
                  path="/aboutus"
                  render={props => <AboutUs {...props} />}
                />
                <Route
                  path="/loggeddata"
                  render={props => <LoggedData {...props} />}
                />
                <Route path="/faq" render={props => <FAQ {...props} />} />
                <Route path="/settings" component={Settings} />
                <Route path="/frontlayout" component={FrontLayout} />
                <Route path="/backlayout" component={BackLayout} />
                <Route path="/devicescreen" component={DeviceScreen} />
              </Switch>
            </Appshell>
            <Snackbar
              anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
              open={snackbar.isOpen}
              onClose={closeSnackbar}
              ContentProps={{
                'aria-describedby': 'snackbar',
              }}
              autoHideDuration={snackbar.timeout}
              message={<span id="snackbar">{snackbar.message}</span>}
            />
            <CustomDialog
              title={dialog.title}
              isOpen={dialog.isOpen}
              variant={dialog.variant}
              hint={dialog.hint}
              textTitle={dialog.textTitle}
              onDialogClose={closeDialog}
              onCheck={dialog.onCheck}
              inputCheck={dialog.inputCheck}
              onAccept={dialog.onAccept}
              onCancel={dialog.onCancel}
            />
          </HashRouter>
        </ThemeProvider>
      </MuiThemeProvider>
    );
  }
}

const mapStateToProps = state => ({ ...state.app, ...state.config });

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      openSnackbar,
      closeSnackbar,
      deviceConnected,
      deviceDisconnected,
      closeDialog,
    },
    dispatch,
  ),
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
