import React from 'react';
import Button from '@material-ui/core/Button';
import ReadIcon from '@material-ui/icons/PlayCircleFilled';
import StopIcon from '@material-ui/icons/PauseCircleFilled';
import RecordIcon from '@material-ui/icons/RadioButtonChecked';
import { withStyles } from '@material-ui/core/styles';
import { ActionButtonContainer } from './ActionButton.styles';

const styles = () => ({
  buttonMargin: {
    margin: '0px 0px 0px 16px',
  },
});

const ActionButtons = ({ isReading, onToggleRead, isConnected, classes }) => {
  return (
    <ActionButtonContainer>
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
    </ActionButtonContainer>
  );
};

export default withStyles(styles)(ActionButtons);
