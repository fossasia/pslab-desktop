import React from 'react';
import { action, actions } from '@storybook/addon-actions';

import CustomDialog from './CustomDialog';

export default {
  title: 'Components/CustomDialog',
  component: CustomDialog,
};

export const SimpleDialog = () => (
  <CustomDialog onDialogClose={action('close')} title="Hello" isOpen />
);

export const InputDialog = () => (
  <CustomDialog
    title="Hello"
    isOpen
    hint="hello :)"
    variant="simple-input"
    inputCheck={a => a.length > 0}
    {...actions('onAccept', 'onCancel', 'onDialogClose')}
  />
);
