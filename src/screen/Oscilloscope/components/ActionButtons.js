import React from 'react';
import { Button, Icon } from '@material-ui/core';
import { ButtonWrapper } from './ActionButtons.styles';

const ActionButtons = ({ isReading, onToggleRead }) => {
  return (
    <ButtonWrapper>
      <Button
        variant="contained"
        size="medium"
        color="primary"
        onClick={onToggleRead}
        style={{ borderRadius: '5px' }}
      >
        <Icon>{isReading ? 'play_arrow' : 'pause'}</Icon>
      </Button>
      <Button
        variant="contained"
        size="medium"
        color="primary"
        onClick={onToggleRead}
        style={{ borderRadius: '5px' }}
      >
        <Icon>cloud_upload</Icon>
      </Button>
    </ButtonWrapper>
  );
};

export default ActionButtons;
