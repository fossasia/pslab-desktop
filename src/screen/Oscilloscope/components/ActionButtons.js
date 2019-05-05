import React from 'react';
import ReadIcon from '@material-ui/icons/PlayCircleFilled';
import StopIcon from '@material-ui/icons/PauseCircleFilled';
import RecordIcon from '@material-ui/icons/RadioButtonChecked';
import { Button } from '@material-ui/core';
import { withStyles, withTheme } from '@material-ui/core/styles';
import { ButtonWrapper } from './ActionButtons.styles';

const styles = theme => ({
  buttonMargin: {
    margin: '0px 0px 0px 16px',
  },
});

const ActionButtons = ({ isConnected, isReading, onToggleRead, classes }) => {
  return (
    <ButtonWrapper>
      <Button
        fullWidth={true}
        variant="contained"
        size="large"
        color="default"
        disabled={!isConnected}
        onClick={onToggleRead}
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

export default withTheme()(withStyles(styles)(ActionButtons));
