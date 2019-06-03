import React from 'react';
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Button,
  TextField,
} from '@material-ui/core';

const CustomDialog = ({
  title,
  isOpen,
  variant,
  hint,
  textTitle,
  onDialogClose,
  onCheck,
  onAccept,
  onCancel,
}) => {
  const [values, setValues] = React.useState({
    textValue: '',
    isTextError: false,
  });

  const onTextFieldChange = fieldName => event => {
    setValues({
      ...values,
      [fieldName]: event.target.value,
      isTextError: false,
    });
  };

  const onReset = () => {
    setValues({
      textValue: '',
      isTextError: false,
    });
  };

  const onHandleAccept = () => {
    const isError = onCheck ? onCheck(values.textValue) : false;
    if (isError) {
      setValues({
        ...values,
        isTextError: true,
      });
    } else {
      onAccept(values.textValue);
      onReset();
      onDialogClose();
    }
  };

  const onHandleCancel = () => {
    onCancel && onCancel();
    onReset();
    onDialogClose();
  };

  const onHandleClose = () => {
    onReset();
    onDialogClose();
  };

  const renderDialogContent = () => {
    switch (variant) {
      case 'simple-input':
        return (
          <DialogContent>
            {hint && <DialogContentText>{hint}</DialogContentText>}
            <TextField
              autoFocus
              margin="dense"
              id="name"
              label={textTitle}
              type="number"
              value={values.textValue}
              onChange={onTextFieldChange('textValue')}
              fullWidth
            />
          </DialogContent>
        );
      default:
        break;
    }
  };

  const renderDialogAction = () => {
    switch (variant) {
      case 'simple-input':
        return (
          <DialogActions>
            <Button onClick={onHandleCancel} color="primary">
              Cancel
            </Button>
            <Button onClick={onHandleAccept} color="primary">
              Accept
            </Button>
          </DialogActions>
        );
      default:
        break;
    }
  };

  return (
    <Dialog
      open={isOpen}
      onClose={onHandleClose}
      aria-labelledby="form-dialog-title"
    >
      {title && <DialogTitle id="form-dialog-title">{title}</DialogTitle>}
      {renderDialogContent()}
      {renderDialogAction()}
    </Dialog>
  );
};

export default CustomDialog;
