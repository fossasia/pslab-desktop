import React, { useState } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Link, withRouter } from 'react-router-dom';
import {
  IconButton,
  Tooltip,
  Drawer,
  List,
  Divider,
  ListItem,
  ListItemText,
  ListItemIcon,
  Menu,
  MenuItem,
} from '@material-ui/core';
import { withStyles, withTheme } from '@material-ui/core/styles';
import {
  Settings as SettingIcon,
  Refresh as ResetIcon,
  Feedback as FeedbackIcon,
  Error as AboutUsIcon,
  WifiTethering as LoggedDataIcon,
  ViewComfy as InstrumentsIcon,
  ArrowBack as BackIcon,
  DeveloperBoard as DeviceIcon,
  Menu as DrawerIcon,
  SaveAlt as ImportIcon,
  MoreVert as LayoutIcon,
  RadioButtonChecked as StartRecordIcon,
  Stop as StopRecordIcon,
  ShoppingCart as CartIcon,
} from '@material-ui/icons';
import { extractFileName } from '../../utils/fileNameProcessor';
import { Save as SaveIcon } from '@material-ui/icons';
import AppIcon from '../../resources/app_icon.png';
import {
  AppshellContainer,
  ChildrenContainer,
  Spacer,
  ChildrenWrapper,
  ButtonContainer,
  TitleContainer,
  AppBar,
  ButtonTextModifier,
  RecText,
} from './Appshell.styles';
import DisconnectedIcon from '../../resources/device_disconnected.svg';
import ConnectedIcon from '../../resources/device_connected.svg';
import { openSnackbar } from '../../redux/actions/app';

const electron = window.require('electron');
const { remote } = window.require('electron');
const { ipcRenderer } = electron;
const fs = remote.require('fs');
const { dialog } = remote;
const loadBalancer = window.require('electron-load-balancer');

const styles = theme => ({
  iconButton: {
    color: theme.pallet.common.white,
  },
  list: {
    width: 250,
  },
  fullList: {
    width: 'auto',
  },
});

const Appshell = ({
  device,
  reset,
  children,
  history,
  location,
  classes,
  dataPath,
  openSnackbar,
  isWriting,
  startWriting,
  stopWriting,
}) => {
  const [drawerOpen, toggleDrawer] = useState(false);
  const [menuOpen, toggleMenu] = useState(null);

  const openImportWindow = () => {
    dialog.showOpenDialog(
      null,
      {
        title: 'Select file to import',
        properties: ['openFile'],
        filters: [{ name: 'Data File', extensions: ['csv'] }],
      },
      filePath => {
        if (filePath) {
          const fileName = extractFileName(filePath[0]);
          fs.copyFile(filePath[0], `${dataPath}/${fileName}`, err => {
            if (err) {
              openSnackbar({ message: 'Import failed' });
            }
            openSnackbar({ message: 'Import successful' });
          });
        }
      },
    );
  };

  const layoutButtonRenderer = location => {
    if (
      location.pathname === '/' ||
      location.pathname === '/frontlayout' ||
      location.pathname === '/backlayout'
    ) {
      return (
        <div>
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={event => {
              toggleMenu(event.currentTarget);
            }}
          >
            <LayoutIcon />
          </IconButton>
          <Menu
            id="simple-menu"
            anchorEl={menuOpen}
            keepMounted
            open={Boolean(menuOpen)}
            onClose={() => toggleMenu(null)}
          >
            <MenuItem
              onClick={() => {
                toggleMenu(null);
                history.push('/frontlayout');
              }}
            >
              Front Layout
            </MenuItem>
            <MenuItem
              onClick={() => {
                toggleMenu(null);
                history.push('/backlayout');
              }}
            >
              Back Layout
            </MenuItem>
          </Menu>
        </div>
      );
    }
  };

  const saveButtonRenderer = location => {
    switch (location.pathname) {
      case '/wavegenerator':
        return (
          <IconButton
            disabled={!device.isConnected}
            className={classes.iconButton}
            size="medium"
            onClick={() => {
              loadBalancer.sendData(ipcRenderer, 'linker', {
                command: 'SAVE_CONFIG_WAV_GEN',
                dataPath: dataPath,
              });
            }}
          >
            <SaveIcon />
          </IconButton>
        );
      case '/powersource':
        return (
          <IconButton
            disabled={!device.isConnected}
            className={classes.iconButton}
            size="medium"
            onClick={() => {
              loadBalancer.sendData(ipcRenderer, 'linker', {
                command: 'SAVE_CONFIG_PWR_SRC',
                dataPath: dataPath,
              });
            }}
          >
            <SaveIcon />
          </IconButton>
        );
      case '/robotarm':
        return (
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={() => {
              loadBalancer.start(ipcRenderer, 'playback');
              setTimeout(() => {
                loadBalancer.sendData(ipcRenderer, 'playback', {
                  command: 'SAVE_CONFIG_ROB_ARM',
                });
              }, 500);
            }}
          >
            <SaveIcon />
          </IconButton>
        );
      case '/logicanalyzer':
        return (
          <IconButton
            className={classes.iconButton}
            size="medium"
            disabled={!device.isConnected}
            onClick={() => {
              loadBalancer.start(ipcRenderer, 'playback');
              setTimeout(() => {
                loadBalancer.sendData(ipcRenderer, 'playback', {
                  command: 'SAVE_DATA_LA',
                });
              }, 500);
            }}
          >
            <SaveIcon />
          </IconButton>
        );
      case '/multimeter':
        return isWriting ? (
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={() => stopWriting()}
          >
            <StopRecordIcon />
          </IconButton>
        ) : (
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={() => startWriting('Multimeter')}
            disabled={!device.isConnected}
          >
            <ButtonTextModifier>
              <StartRecordIcon />
              <RecText>Rec</RecText>
            </ButtonTextModifier>
          </IconButton>
        );
      case '/oscilloscope':
        return isWriting ? (
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={() => stopWriting()}
          >
            <StopRecordIcon />
          </IconButton>
        ) : (
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={() => startWriting('Oscilloscope')}
            disabled={!device.isConnected}
          >
            <ButtonTextModifier>
              <StartRecordIcon />
              <RecText>Rec</RecText>
            </ButtonTextModifier>
          </IconButton>
        );
      case '/loggeddata':
        return (
          <IconButton
            className={classes.iconButton}
            size="medium"
            onClick={openImportWindow}
          >
            <ImportIcon />
          </IconButton>
        );
      default:
        return undefined;
    }
  };

  const titleRenderer = location => {
    switch (location.pathname) {
      case '/wavegenerator':
        return 'Wave Generator';
      case '/powersource':
        return 'Power Source';
      case '/robotarm':
        return 'Robot Arm';
      case '/multimeter':
        return 'Multimeter';
      case '/oscilloscope':
        return 'Oscilloscope';
      case '/logicanalyzer':
        return 'Logic Analyzer';
      case '/loggeddata':
        return 'Data Logger';
      case '/sensors':
        return 'Sensors';
      case '/aboutus':
        return 'About Us';
      case '/faq':
        return 'FAQ';
      case '/settings':
        return 'Settings';
      case '/devicescreen':
        return 'Device Status';
      case '/frontlayout':
        return 'Front Pin Layout';
      case 'backlayout':
        return 'Back Pin Layout';
      default:
        return 'Pocket Science Lab - PSLab';
    }
  };

  return (
    <AppshellContainer>
      <Drawer open={drawerOpen} onClose={() => toggleDrawer(!drawerOpen)}>
        <div className={classes.list} role="presentation">
          <div
            style={{
              borderRadius: '50%',
              border: '3px solid #000',
              width: '8.2em',
              height: '8.2em',
              margin: '16px 0px 8px 32px',
            }}
          >
            <img
              alt="App"
              src={AppIcon}
              style={{
                height: '6.5em',
                width: 'auto',
                margin: '8px 8px 8px 10px',
              }}
            />
          </div>
          <div
            style={{
              color: '#000',
              fontSize: '18px',
              margin: '16px 0px 16px 32px',
            }}
          >
            {device.isConnected ? 'Connected' : 'Not Connected'}
          </div>
        </div>
        <div
          className={classes.list}
          role="presentation"
          onClick={() => toggleDrawer(!drawerOpen)}
          onKeyDown={() => toggleDrawer(!drawerOpen)}
        >
          <List>
            <Link to="/">
              <ListItem button>
                <ListItemIcon>
                  <InstrumentsIcon />
                </ListItemIcon>
                <ListItemText primary={'Instruments'} />
              </ListItem>
            </Link>
            <Link to="/loggeddata">
              <ListItem button>
                <ListItemIcon>
                  <LoggedDataIcon />
                </ListItemIcon>
                <ListItemText primary={'Logged Data'} />
              </ListItem>
            </Link>
            <Divider />
            <Link to="/devicescreen">
              <ListItem button>
                <ListItemIcon>
                  <DeviceIcon />
                </ListItemIcon>
                <ListItemText primary={'Connected Device'} />
              </ListItem>
            </Link>
            <Link to="/settings">
              <ListItem button>
                <ListItemIcon>
                  <SettingIcon />
                </ListItemIcon>
                <ListItemText primary={'Settings'} />
              </ListItem>
            </Link>
          </List>
          <Divider />
          <Link to="/aboutus">
            <ListItem button>
              <ListItemIcon>
                <AboutUsIcon />
              </ListItemIcon>
              <ListItemText primary={'About Us'} />
            </ListItem>
          </Link>
          <ListItem
            button
            onClick={() => {
              window.open(
                'https://pslab.io/',
                '_blank',
                'height=650,width=1000,frame=true,show=true',
              );
            }}
          >
            <ListItemIcon>
              <CartIcon />
            </ListItemIcon>
            <ListItemText primary={'Buy PSLab'} />
          </ListItem>
          <List>
            <Link to="/faq">
              <ListItem button>
                <ListItemIcon>
                  <FeedbackIcon />
                </ListItemIcon>
                <ListItemText primary={'FAQs'} />
              </ListItem>
            </Link>
          </List>
        </div>
      </Drawer>
      <ChildrenContainer>
        <AppBar>
          <ButtonContainer>
            <IconButton
              onClick={() => toggleDrawer(true)}
              className={classes.iconButton}
              size="medium"
            >
              <DrawerIcon style={{ fontSize: 24 }} />
            </IconButton>
            {location.pathname !== '/' ? (
              <IconButton
                className={classes.iconButton}
                size="medium"
                onClick={() => history.goBack()}
              >
                <BackIcon style={{ fontSize: 24 }} />
              </IconButton>
            ) : (
              ''
            )}
          </ButtonContainer>
          <TitleContainer>{titleRenderer(location)}</TitleContainer>
          <Spacer />
          <ButtonContainer>
            <Tooltip title="Reset">
              <IconButton
                disabled={!device.isConnected}
                onClick={reset}
                className={classes.iconButton}
                size="medium"
              >
                <ResetIcon style={{ fontSize: 24 }} />
              </IconButton>
            </Tooltip>
            <Tooltip
              title={
                device.deviceInformation
                  ? `Device name: ${device.deviceInformation.deviceName} Port: ${device.deviceInformation.portName}`
                  : 'No device connected'
              }
            >
              <IconButton className={classes.iconButton} size="medium">
                {device.isConnected ? (
                  <img
                    alt="Connected"
                    src={ConnectedIcon}
                    style={{ height: '20px', width: '20px' }}
                  />
                ) : (
                  <img
                    alt="Disconnected"
                    src={DisconnectedIcon}
                    style={{ height: '20px', width: '20px' }}
                  />
                )}
              </IconButton>
            </Tooltip>
            {saveButtonRenderer(location)}
            {layoutButtonRenderer(location)}
          </ButtonContainer>
        </AppBar>
        <ChildrenWrapper>{children}</ChildrenWrapper>
      </ChildrenContainer>
    </AppshellContainer>
  );
};

const mapStateToProps = state => state.app;

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      openSnackbar,
    },
    dispatch,
  ),
});

export default withRouter(
  withTheme()(
    withStyles(styles)(connect(mapStateToProps, mapDispatchToProps)(Appshell)),
  ),
);
