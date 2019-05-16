import React from 'react';
import {
  CircularInput,
  CircularTrack,
  CircularProgress,
  CircularThumb,
} from 'react-circular-input';
import { Spring } from 'react-spring/renderprops';
import { withTheme } from 'styled-components';

const CustomCircularInput = ({
  steps,
  setValue,
  value,
  min = 0,
  max = 100,
  step,
  radius,
  theme,
  selector = false,
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
          <CircularTrack strokeWidth={5} stroke={theme.primary.light} />
          {!selector && (
            <CircularProgress strokeWidth={15} stroke={theme.secondary.dark} />
          )}
          {selector && <CircularThumb r={12} fill={theme.secondary.dark} />}
        </CircularInput>
      )}
    </Spring>
  );
};

export default withTheme(CustomCircularInput);
