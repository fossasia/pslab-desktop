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
  Usb as ConnectedIcon,
  Warning as DisconnectedIcon,
  Settings as SettingIcon,
  Refresh as ResetIcon,
  BugReport as BugIcon,
  Feedback as FeedbackIcon,
  Error as AboutUsIcon,
  WifiTethering as LoggedDataIcon,
  ViewComfy as InstrumentsIcon,
  ArrowBack as BackIcon,
  DeveloperBoard as DeviceIcon,
  Menu as DrawerIcon,
  SaveAlt as ImportIcon,
  MoreVert as LayoutIcon,
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
} from './Appshell.styles';
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

  return (
    <AppshellContainer>
      <Drawer open={drawerOpen} onClose={() => toggleDrawer(!drawerOpen)}>
        <div className={classes.list} role="presentation">
          <img
            src={AppIcon}
            style={{ height: '8em', width: 'auto', margin: '32px' }}
          />
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
            <ListItem button>
              <ListItemIcon>
                <DeviceIcon />
              </ListItemIcon>
              <ListItemText primary={'Device'} />
            </ListItem>
            <Link to="/loggeddata">
              <ListItem button>
                <ListItemIcon>
                  <LoggedDataIcon />
                </ListItemIcon>
                <ListItemText primary={'Logged Data'} />
              </ListItem>
            </Link>
            <ListItem button>
              <ListItemIcon>
                <SettingIcon />
              </ListItemIcon>
              <ListItemText primary={'Settings'} />
            </ListItem>
          </List>
          <Divider />
          <List>
            <Link to="/faq">
              <ListItem button>
                <ListItemIcon>
                  <FeedbackIcon />
                </ListItemIcon>
                <ListItemText primary={'FAQs'} />
              </ListItem>
            </Link>
            <Link to="/aboutus">
              <ListItem button>
                <ListItemIcon>
                  <AboutUsIcon />
                </ListItemIcon>
                <ListItemText primary={'About Us'} />
              </ListItem>
            </Link>
            <ListItem button>
              <ListItemIcon>
                <BugIcon />
              </ListItemIcon>
              <ListItemText primary={'Feedback & Bugs'} />
            </ListItem>
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
            <IconButton
              className={classes.iconButton}
              size="medium"
              onClick={() => history.goBack()}
            >
              <BackIcon style={{ fontSize: 24 }} />
            </IconButton>
          </ButtonContainer>
          <TitleContainer />
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
                  <ConnectedIcon style={{ fontSize: 24 }} />
                ) : (
                  <DisconnectedIcon style={{ fontSize: 24 }} />
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
    withStyles(styles)(
      connect(
        mapStateToProps,
        mapDispatchToProps,
      )(Appshell),
    ),
  ),
);
