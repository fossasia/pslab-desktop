import {
  OPEN_DIALOG,
  CLOSE_DIALOG,
  OPEN_SNACKBAR,
  CLOSE_SNACKBAR,
  DEVICE_CONNECTED,
  DEVICE_DISCONNECTED,
} from '../actionTypes/app';

export const deviceConnected = ({ deviceInformation }) => {
  return {
    type: DEVICE_CONNECTED,
    payload: { deviceInformation },
  };
};

export const deviceDisconnected = () => {
  return {
    type: DEVICE_DISCONNECTED,
  };
};

export const openSnackbar = ({ message = '', timeout = 4000 }) => {
  return {
    type: OPEN_SNACKBAR,
    payload: {
      message,
      timeout,
    },
  };
};

export const closeSnackbar = () => {
  return {
    type: CLOSE_SNACKBAR,
  };
};

export const openDialog = ({
  variant = null,
  title = null,
  hint = null,
  textTitle = null,
  onCheck = null,
  inputCheck = null,
  onAccept = null,
  onCancel = null,
}) => {
  return {
    type: OPEN_DIALOG,
    payload: {
      variant,
      title,
      hint,
      textTitle,
      onCheck,
      inputCheck,
      onAccept,
      onCancel,
    },
  };
};

export const closeDialog = () => {
  return {
    type: CLOSE_DIALOG,
  };
};
