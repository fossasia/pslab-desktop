import React from 'react';
import ReadIcon from '@material-ui/icons/PlayCircleFilled';
import StopIcon from '@material-ui/icons/PauseCircleFilled';
import RecordIcon from '@material-ui/icons/RadioButtonChecked';
import { Button } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import { ButtonWrapper } from './ActionButtons.styles';

const styles = () => ({
  buttonMargin: {
    margin: '0px 0px 0px 16px',
  },
});

const ActionButtons = ({ isConnected, isReading, toggleRead, classes }) => {
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

export default withStyles(styles)(ActionButtons);
