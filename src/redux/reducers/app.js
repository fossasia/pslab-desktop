import {
  OPEN_SNACKBAR,
  CLOSE_SNACKBAR,
  DEVICE_CONNECTED,
  DEVICE_DISCONNECTED,
  OPEN_DIALOG,
  CLOSE_DIALOG,
} from '../actionTypes/app';

const initialState = {
  device: {
    isConnected: false,
    deviceInformation: null,
  },
  snackbar: {
    isOpen: false,
    message: '',
    timeout: 4000,
  },
  dialog: {
    isOpen: false,
    variant: null,
    title: null,
    hint: null,
    textTitle: null,
    onCheck: null,
    inputCheck: null,
    onAccept: null,
    onCancel: null,
  },
};

export const appReducer = (prevState = initialState, action) => {
  switch (action.type) {
    case OPEN_SNACKBAR: {
      const { message, timeout } = action.payload;
      return {
        ...prevState,
        snackbar: {
          isOpen: true,
          message,
          timeout,
        },
      };
    }
    case CLOSE_SNACKBAR: {
      return {
        ...prevState,
        snackbar: {
          ...initialState.snackbar,
        },
      };
    }
    case DEVICE_CONNECTED: {
      const { deviceInformation } = action.payload;
      return {
        ...prevState,
        device: {
          isConnected: true,
          deviceInformation: {
            ...initialState.device.deviceInformation,
            ...deviceInformation,
          },
        },
      };
    }
    case DEVICE_DISCONNECTED: {
      return {
        ...prevState,
        device: {
          ...initialState.device,
        },
      };
    }
    case OPEN_DIALOG: {
      const {
        variant,
        title,
        hint,
        textTitle,
        onCheck,
        inputCheck,
        onAccept,
        onCancel,
      } = action.payload;
      return {
        ...prevState,
        dialog: {
          isOpen: true,
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
    }
    case CLOSE_DIALOG: {
      return {
        ...prevState,
        dialog: {
          ...initialState.dialog,
        },
      };
    }
    default:
      return initialState;
  }
};
