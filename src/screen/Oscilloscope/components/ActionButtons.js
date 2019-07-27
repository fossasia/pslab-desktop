import React from 'react';
import {
  Pause as StopReadIcon,
  PlayCircleFilled as ReadIcon,
  RadioButtonChecked as RecordIcon,
  Stop as StopIcon,
} from '@material-ui/icons';
import { Button } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import { ButtonWrapper } from './ActionButtons.styles';

const styles = () => ({
  buttonMargin: {
    margin: '0px 0px 0px 16px',
  },
});

const ActionButtons = ({
  isConnected,
  isReading,
  isWriting,
  onToggleRead,
  onToggleWrite,
  classes,
}) => {
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
          <StopReadIcon style={{ fontSize: 20 }} />
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
        disabled={!isConnected || isReading}
        onClick={onToggleWrite}
      >
        {isWriting ? (
          <StopIcon style={{ fontSize: 20 }} />
        ) : (
          <RecordIcon style={{ fontSize: 20 }} />
        )}
      </Button>
    </ButtonWrapper>
  );
};

export default withStyles(styles)(ActionButtons);
