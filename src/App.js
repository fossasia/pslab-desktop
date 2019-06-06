import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
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
import { MuiThemeProvider } from '@material-ui/core/styles';
import { ThemeProvider } from 'styled-components';
import theme from './theme';

const electron = window.require('electron');

const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isConnected: false,
      deviceInformation: null,
      snackbar: {
        isOpen: false,
        message: '',
        timeout: 4000,
      },
      dialog: {
        isOpen: false,
        variant: null,
        title: null,
        hint: null,
        textTitle: null,
        onCheck: null,
        onAccept: null,
        onCancel: null,
      },
    };
  }

  onOpenDialog = ({
    variant,
    title,
    hint,
    textTitle,
    onCheck,
    onAccept,
    onCancel,
  }) => () => {
    this.setState(prevState => ({
      ...prevState,
      dialog: {
        ...prevState.dialog,
        isOpen: true,
        variant,
        title,
        hint,
        onCheck,
        textTitle,
        onAccept,
        onCancel,
      },
    }));
  };

  onCloseDialog = () => {
    this.setState(prevState => ({
      ...prevState,
      dialog: {
        ...prevState.dialog,
        isOpen: false,
        variant: null,
        title: null,
        hint: null,
        onCheck: null,
        textTitle: null,
        onAccept: null,
        onCancel: null,
      },
    }));
  };

  onOpenSnackBar = ({ message, timeout = 2500, variant }) => {
    this.setState(prevState => ({
      ...prevState,
      snackbar: {
        ...prevState.snackbar,
        isOpen: true,
        message,
      },
    }));
  };

  onCloseSnackBar = () => {
    this.setState(prevState => ({
      ...prevState,
      snackbar: {
        ...prevState.snackbar,
        isOpen: false,
        message: '',
      },
    }));
  };

  componentDidMount() {
    window.onbeforeunload = event => {
      loadBalancer.stopAllBackgroundProcess();
    };

    ipcRenderer.on('TO_RENDERER_STATUS', (event, args) => {
      const { isConnected, message, deviceName, portName } = args;
      this.state.isConnected !== isConnected &&
        this.setState({
          isConnected,
          deviceInformation: deviceName
            ? {
                deviceName,
                portName,
              }
            : null,
        });

      if (!isConnected) {
        loadBalancer.stopBackgroundProcess(ipcRenderer, 'linker');
        if (!this.reconnect) {
          this.onOpenSnackBar({ message });
          this.reconnect = setInterval(() => {
            loadBalancer.startBackgroundProcess(ipcRenderer, 'linker');
          }, 2500);
        }
      } else {
        this.onOpenSnackBar({ message });
        clearInterval(this.reconnect);
        this.reconnect = false;
      }
    });
    loadBalancer.startBackgroundProcess(ipcRenderer, 'linker');

    // ipcRenderer.on('DEBUG', (event, args) => {
    //   console.log(args);
    // });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('TO_RENDERER_STATUS');
    loadBalancer.stopBackgroundProcess(ipcRenderer, 'linker');
  }

  render() {
    const { isConnected, deviceInformation, snackbar, dialog } = this.state;

    return (
      <MuiThemeProvider theme={theme}>
        <ThemeProvider theme={theme.pallet}>
          <HashRouter>
            <Appshell
              isConnected={isConnected}
              deviceInformation={deviceInformation}
            >
              <Switch>
                <Route path="/" exact component={Home} />
                <Route
                  path="/oscilloscope"
                  render={props => (
                    <Oscilloscope {...props} isConnected={isConnected} />
                  )}
                />
                <Route path="/logicanalyser" component={LogicAnalyser} />
                <Route
                  path="/powersource"
                  render={props => (
                    <PowerSource
                      {...props}
                      isConnected={isConnected}
                      onOpenDialog={this.onOpenDialog}
                    />
                  )}
                />
                <Route
                  path="/wavegenerator"
                  render={props => (
                    <WaveGenerator {...props} isConnected={isConnected} />
                  )}
                />
                <Route
                  path="/multimeter"
                  render={props => (
                    <Multimeter {...props} isConnected={isConnected} />
                  )}
                />
                <Route path="/settings" component={Settings} />
              </Switch>
            </Appshell>
            <Snackbar
              anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
              open={snackbar.isOpen}
              onClose={this.onCloseSnackBar}
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
              onDialogClose={this.onCloseDialog}
              onCheck={dialog.onCheck}
              onAccept={dialog.onAccept}
              onCancel={dialog.onCancel}
            />
          </HashRouter>
        </ThemeProvider>
      </MuiThemeProvider>
    );
  }
}

export default App;
