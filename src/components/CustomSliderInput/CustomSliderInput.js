import React from 'react';
import Slider from '@material-ui/lab/Slider';
import { withStyles } from '@material-ui/core/styles';

const styles = () => ({
  slider: {
    margin: '0px 8px 0px 8px',
  },
});

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
        style={{
          margin: '0px 0px 0px 8px',
          whiteSpace: 'nowrap',
          minWidth: minUnitWidth,
          textAlign: 'right',
        }}
      >{`${display ? display : value} ${unit}`}</span>
    </div>
  );
};

export default withStyles(styles)(CustomSliderInput);
