import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import Slider from '@material-ui/lab/Slider';
import { withStyles } from '@material-ui/core/styles';
import { openDialog } from '../../redux/actions/app';

const styles = () => ({
  slider: {
    margin: '0px 8px 0px 8px',
  },
});

const onCheck = (min, max) => value => {
  return !(value >= min && value <= max);
};

const CustomSliderInput = ({
  title,
  unit,
  onChangeSlider,
  value,
  min,
  max,
  inputCheck,
  step,
  disabled,
  minTitleWidth,
  minUnitWidth,
  display,
  classes,
  openDialog,
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
        onClick={() => {
          !disabled &&
            openDialog({
              variant: 'simple-input',
              title: title,
              textTitle: `Enter value (${min} to ${max})`,
              onAccept: value => {
                onChangeSlider(undefined, value);
              },
              onCheck: onCheck(min, max),
              inputCheck: inputCheck,
              onCancel: () => {},
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
    </div>
  );
};

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      openDialog,
    },
    dispatch,
  ),
});

export default withStyles(styles)(
  connect(null, mapDispatchToProps)(CustomSliderInput),
);
