import React from 'react';
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
        disabled={!isConnected}
        onClick={toggleRead}
        style={{ color: '#d32f2f' }}
      >
        {isReading ? <b>ANALYZING</b> : <b>ANALYZE</b>}
      </Button>
    </ButtonWrapper>
  );
};

export default withStyles(styles)(ActionButtons);
