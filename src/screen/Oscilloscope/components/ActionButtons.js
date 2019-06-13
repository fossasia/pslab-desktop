import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Button } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import ReadIcon from '@material-ui/icons/PlayCircleFilled';
import StopIcon from '@material-ui/icons/PauseCircleFilled';
import RecordIcon from '@material-ui/icons/RadioButtonChecked';
import { ButtonWrapper } from './ActionButtons.styles';
import { toggleRead } from '../../../redux/actions/oscilloscope';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

const styles = () => ({
  buttonMargin: {
    margin: '0px 0px 0px 16px',
  },
});

const ActionButtons = ({ isConnected, isReading, toggleRead, classes }) => {
  useEffect(() => {
    if (isConnected) {
      isReading
        ? loadBalancer.sendData(ipcRenderer, 'linker', {
            command: 'START_OSC',
          })
        : loadBalancer.sendData(ipcRenderer, 'linker', {
            command: 'STOP_OSC',
          });
    }
  }, [isReading]);

  return (
    <ButtonWrapper>
      <Button
        fullWidth={true}
        variant="contained"
        size="large"
        color="default"
        disabled={!isConnected}
        onClick={toggleRead}
      >
        {isReading ? (
          <StopIcon style={{ fontSize: 20 }} />
        ) : (
          <ReadIcon style={{ fontSize: 20 }} />
        )}
      </Button>
      <Button
        className={classes.buttonMargin}
        fullWidth={true}
        variant="contained"
        size="large"
        color="default"
      >
        <RecordIcon style={{ fontSize: 20 }} />
      </Button>
    </ButtonWrapper>
  );
};

const mapStateToProps = state => {
  const { isReading } = state.oscilloscope;
  const { isConnected } = state.app.device;
  return {
    isConnected,
    isReading,
  };
};

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      toggleRead,
    },
    dispatch,
  ),
});

export default withStyles(styles)(
  connect(
    mapStateToProps,
    mapDispatchToProps,
  )(ActionButtons),
);
