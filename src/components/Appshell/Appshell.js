import React from 'react';
import { connect } from 'react-redux';
import { Link, withRouter } from 'react-router-dom';
import { IconButton, Tooltip } from '@material-ui/core';
import { withStyles, withTheme } from '@material-ui/core/styles';
import ConnectedIcon from '@material-ui/icons/Usb';
import DisconnectedIcon from '@material-ui/icons/Warning';
import OscilloscopeIcon from '@material-ui/icons/ViewComfy';
import LogicAnalyserIcon from '@material-ui/icons/InsertChart';
import PowerSourceIcon from '@material-ui/icons/FlashOn';
import WaveGeneratorIcon from '@material-ui/icons/GraphicEq';
import MultimeterIcon from '@material-ui/icons/DeveloperBoard';
import SettingIcon from '@material-ui/icons/Settings';
import {
  AppshellContainer,
  ChildrenContainer,
  NavigationContainer,
  TopNavigationWrapper,
  BottomNavigationWrapper,
  Spacer,
  NavigationTab,
  AppIconWrapper,
  ChildrenWrapper,
  ButtonContainer,
  TitleContainer,
  AppBar,
} from './Appshell.styles';
import AppIcon from '../../resources/app_icon.svg';

const styles = theme => ({
  iconButton: {
    color: theme.pallet.common.white,
  },
});

const topNavigationItems = [
  {
    name: 'Oscilloscope',
    redirectPath: '/oscilloscope',
    icon: <OscilloscopeIcon style={{ fontSize: '2.2em' }} />,
  },
  {
    name: 'Logica Analyser',
    redirectPath: '/logicanalyser',
    icon: <LogicAnalyserIcon style={{ fontSize: '2.2em' }} />,
  },
  {
    name: 'Power Source',
    redirectPath: '/powersource',
    icon: <PowerSourceIcon style={{ fontSize: '2.2em' }} />,
  },
  {
    name: 'Wave Generator',
    redirectPath: '/wavegenerator',
    icon: <WaveGeneratorIcon style={{ fontSize: '2.2em' }} />,
  },
  {
    name: 'Multimeter',
    redirectPath: '/multimeter',
    icon: <MultimeterIcon style={{ fontSize: '2.2em' }} />,
  },
];

const Appshell = ({ children, location, device, classes }) => {
  return (
    <AppshellContainer>
      <NavigationContainer>
        <AppIconWrapper>
          <img
            style={{
              height: '3em',
              width: 'auto',
            }}
            alt="App Icon"
            src={AppIcon}
          />
        </AppIconWrapper>
        <TopNavigationWrapper>
          {topNavigationItems.map((item, index) => {
            return (
              <Link key={index} to={item.redirectPath}>
                <NavigationTab
                  selected={item.redirectPath === location.pathname}
                >
                  {item.icon}
                </NavigationTab>
              </Link>
            );
          })}
        </TopNavigationWrapper>
        <Spacer />
        <BottomNavigationWrapper>
          <Link to="/settings">
            <NavigationTab>
              <SettingIcon style={{ fontSize: '2.2em' }} />
            </NavigationTab>
          </Link>
        </BottomNavigationWrapper>
      </NavigationContainer>
      <ChildrenContainer>
        <AppBar>
          <TitleContainer />
          <Spacer />
          <ButtonContainer>
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
