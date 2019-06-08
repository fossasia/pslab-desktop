import React from 'react';
import Slider from '@material-ui/lab/Slider';
import { withStyles } from '@material-ui/core/styles';
import CustomDialog from '../CustomDialog/CustomDialog';
const styles = () => ({
  slider: {
    margin: '0px 8px 0px 8px',
  },
});

const onCheck = (min, max) => value => {
  return value >= min && value <= max ? false : true;
};

const CustomSliderInput = ({
  title,
  unit,
  onChangeSlider,
  value,
  min,
  max,
  step,
  disabled,
  minTitleWidth,
  minUnitWidth,
  display,
  classes,
}) => {
  const [values, setValues] = React.useState({
    isDialogOpen: false,
  });
  return (
    <div
      style={{
        display: 'flex',
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <span
        style={{
          margin: '0px 8px 0px 0px',
          whiteSpace: 'nowrap',
          minWidth: minTitleWidth,
        }}
      >
        {title}
      </span>
      <Slider
        className={classes.slider}
        step={step}
        value={value}
        min={min}
        max={max}
        onChange={onChangeSlider}
        disabled={disabled}
      />
      <span
        onClick={() => {
          if (!disabled)
            setValues({
              ...values,
              isDialogOpen: true,
            });
        }}
        style={{
          margin: '0px 0px 0px 8px',
          whiteSpace: 'nowrap',
          minWidth: minUnitWidth,
          textAlign: 'right',
          cursor: 'pointer',
        }}
      >{`${display ? display : value} ${unit}`}</span>
      <CustomDialog
        variant={'simple-input'}
        title={title}
        textTitle={`Enter value (${min} to ${max})`}
        isOpen={!disabled && values.isDialogOpen}
        onDialogClose={() => {
          setValues({
            ...values,
            isDialogOpen: false,
          });
        }}
        onAccept={value => {
          onChangeSlider(undefined, value);
        }}
        onCheck={onCheck(min, max)}
        onCancel={() => {}}
      />
    </div>
  );
};

export default withStyles(styles)(CustomSliderInput);
