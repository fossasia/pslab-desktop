import React from 'react';
import {
  CircularInput,
  CircularTrack,
  CircularProgress,
  CircularThumb,
} from 'react-circular-input';
import { fade } from '@material-ui/core/styles/colorManipulator';
import { Spring } from 'react-spring/renderprops';
import { withTheme } from 'styled-components';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { openDialog } from '../../redux/actions/app';

const CustomCircularInput = ({
  setValue,
  value,
  min = 0,
  max = 100,
  step,
  radius,
  theme,
  selector = false,
  text = false,
  title,
  openDialog,
}) => {
  const rangedValue = v => {
    return (v - min) / (max - min);
  };

  const stepValue = v => {
    if (!step) {
      return min + v * (max - min);
    }
    const increment = v * (max - min);
    const originalMultiplier = Math.round(increment / step);
    return min + originalMultiplier * step;
  };

  return (
    <Spring to={{ value }}>
      {props => (
        <CircularInput
          radius={radius}
          value={rangedValue(props.value)}
          onChange={value => setValue(stepValue(value))}
        >
          <CircularTrack
            strokeWidth={5}
            stroke={fade(theme.primary.light, 0.5)}
          />
          {!selector && (
            <CircularProgress strokeWidth={15} stroke={theme.primary.main} />
          )}
          {selector && <CircularThumb r={12} fill={theme.primary.dark} />}
          {text && (
            <text
              x={100}
              y={100}
              textAnchor="middle"
              dy="0.5em"
              dx="0.3em"
              fontSize="4em"
              onClick={e => {
                e.stopPropagation();
                openDialog({
                  variant: 'simple-input',
                  title: title,
                  textTitle: `Enter value ( ${min} to ${max} )`,
                  onAccept: value => setValue(parseInt(value, 10)),
                  onCheck: value => !(value >= min && value <= max),
                  inputCheck: () => true,
                  onCancel: () => {},
                });
              }}
            >
              {value}°
            </text>
          )}
        </CircularInput>
      )}
    </Spring>
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

export default withTheme(
  connect(null, mapDispatchToProps)(CustomCircularInput),
);
