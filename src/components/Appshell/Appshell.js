import React, { useState } from 'react';
import { connect } from 'react-redux';
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
} from '@material-ui/icons';
import {
  OscilloscopeIcon,
  LogicAnalyserIcon,
  WaveGeneratorIcon,
  PowerSourceIcon,
  MultimeterIcon,
} from '../../components/Icons/PSLabIcons';
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

const topNavigationItems = [
  {
    name: 'Oscilloscope',
    redirectPath: '/oscilloscope',
    icon: <OscilloscopeIcon size={'2em'} />,
  },
  {
    name: 'Logica Analyser',
    redirectPath: '/logicanalyser',
    icon: <LogicAnalyserIcon size={'2em'} />,
  },
  {
    name: 'Power Source',
    redirectPath: '/powersource',
    icon: <PowerSourceIcon size={'2em'} />,
  },
  {
    name: 'Wave Generator',
    redirectPath: '/wavegenerator',
    icon: <WaveGeneratorIcon size={'2em'} />,
  },
  {
    name: 'Multimeter',
    redirectPath: '/multimeter',
    icon: <MultimeterIcon size={'2em'} />,
  },
];

const Appshell = ({ device, reset, children, location, classes }) => {
  const [drawerOpen, toggleDrawer] = useState(false);

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
            <ListItem button>
              <ListItemIcon>
                <LoggedDataIcon />
              </ListItemIcon>
              <ListItemText primary={'Logged Data'} />
            </ListItem>
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
            <Link to="/">
              <IconButton className={classes.iconButton} size="medium">
                <BackIcon style={{ fontSize: 24 }} />
              </IconButton>
            </Link>
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
          </ButtonContainer>
        </AppBar>
        <ChildrenWrapper>{children}</ChildrenWrapper>
      </ChildrenContainer>
    </AppshellContainer>
  );
};

const mapStateToProps = state => state.app;

export default withRouter(
  withTheme()(
    withStyles(styles)(
      connect(
        mapStateToProps,
        null,
      )(Appshell),
    ),
  ),
);
