import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { HashRouter, Route, Switch } from 'react-router-dom';
import { MuiThemeProvider } from '@material-ui/core/styles';
import { ThemeProvider } from 'styled-components';
import Snackbar from '@material-ui/core/Snackbar';
import Appshell from './components/Appshell';
import Home from './screen/Home';
import Oscilloscope from './screen/Oscilloscope';
import LogicAnalyser from './screen/LogicAnalyser';
import PowerSource from './screen/PowerSource';
import WaveGenerator from './screen/WaveGenerator';
import Multimeter from './screen/Multimeter';
import Settings from './screen/Settings';
import CustomDialog from './components/CustomDialog';
import theme from './theme';
import {
  deviceConnected,
  deviceDisconnected,
  openSnackbar,
  closeSnackbar,
  closeDialog,
} from './redux/actions/app';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

const App = ({
  snackbar,
  dialog,
  deviceConnected,
  deviceDisconnected,
  openSnackbar,
  closeSnackbar,
  closeDialog,
  oscilloscope,
}) => {
  useEffect(() => {
    let reconnect = false;
    let oldConnectionStatus = false;
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected, message, deviceName, portName } = args;
      if (oldConnectionStatus !== isConnected) {
        isConnected
          ? deviceConnected({
              deviceInformation: {
                deviceName,
                portName,
              },
            })
          : deviceDisconnected();
        isConnected && setDeviceConfigAll();
        oldConnectionStatus = isConnected;
      }

      if (!isConnected) {
        loadBalancer.stop(ipcRenderer, 'linker');
        if (!reconnect) {
          openSnackbar({ message });
          reconnect = setInterval(() => {
            loadBalancer.start(ipcRenderer, 'linker');
          }, 2500);
        }
      } else {
        openSnackbar({ message });
        clearInterval(reconnect);
        reconnect = false;
      }
    });
    loadBalancer.start(ipcRenderer, 'linker');

    return () => {
      ipcRenderer.removeAllListeners('CONNECTION_STATUS');
      loadBalancer.stop(ipcRenderer, 'linker');
    };
  }, []);

  const setDeviceConfigAll = () => {
    loadBalancer.sendData(ipcRenderer, 'linker', {
      command: 'SET_CONFIG_OSC',
      ...oscilloscope,
      ch1: oscilloscope.activeChannels.ch1,
      ch2: oscilloscope.activeChannels.ch2,
      ch3: oscilloscope.activeChannels.ch3,
      mic: oscilloscope.activeChannels.mic,
    });
  };

  return (
    <MuiThemeProvider theme={theme}>
      <ThemeProvider theme={theme.pallet}>
        <HashRouter>
          <Appshell>
            <Switch>
              <Route path="/" exact component={Home} />
              <Route
                path="/oscilloscope"
                render={props => <Oscilloscope {...props} />}
              />
              <Route path="/logicanalyser" component={LogicAnalyser} />
              <Route
                path="/powersource"
                render={props => <PowerSource {...props} />}
              />
              <Route
                path="/wavegenerator"
                render={props => <WaveGenerator {...props} />}
              />
              <Route
                path="/multimeter"
                render={props => <Multimeter {...props} />}
              />
              <Route path="/settings" component={Settings} />
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
            onAccept={dialog.onAccept}
            onCancel={dialog.onCancel}
          />
        </HashRouter>
      </ThemeProvider>
    </MuiThemeProvider>
  );
};

const mapStateToProps = state => ({
  ...state.app,
  oscilloscope: state.oscilloscope,
});

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      deviceConnected,
      deviceDisconnected,
      openSnackbar,
      closeSnackbar,
      closeDialog,
    },
    dispatch,
  ),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(App);
