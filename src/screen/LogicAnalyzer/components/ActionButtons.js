import React from 'react';
import { Checkbox, FormControlLabel, Button } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import {
  ActionButtonsWrapper,
  ButtonWrapper,
  CheckboxWrapper,
} from './ActionButtons.styles';

const styles = () => ({
  buttonMargin: {
    margin: '0px 0px 0px 16px',
  },
});

const ActionButtons = ({
  isConnected,
  isReading,
  toggleRead,
  isAutoReading,
  toggleAutoRead,
  classes,
}) => {
  return (
    <ActionButtonsWrapper>
      <ButtonWrapper>
        <Button
          fullWidth={true}
          variant="contained"
          size="large"
          disabled={!isConnected}
          onClick={toggleRead}
          style={{ color: '#d32f2f' }}
        >
          {isReading ? <b>ANALYZING</b> : <b>ANALYZE</b>}
        </Button>
      </ButtonWrapper>
      <CheckboxWrapper>
        <FormControlLabel
          control={
            <Checkbox checked={isAutoReading} onChange={toggleAutoRead} />
          }
          label="Auto Recapture"
        />
      </CheckboxWrapper>
    </ActionButtonsWrapper>
  );
};

export default withStyles(styles)(ActionButtons);
