import React from 'react';
import {
  CircularInput,
  CircularTrack,
  CircularProgress,
} from 'react-circular-input';
import { withTheme } from 'styled-components';

const CustomCircularInput = ({
  steps,
  setValue,
  value,
  min = 0,
  max = 100,
  step = 1,
  theme,
}) => {
  const rangedValue = v => {
    return (v - min) / (max - min);
  };

  const stepValue = v => {
    return min + v * (max - min);
  };

  return (
    <CircularInput
      value={rangedValue(value)}
      onChange={value => setValue(stepValue(value))}
    >
      <CircularTrack strokeWidth={5} stroke={theme.primary.light} />
      <CircularProgress strokeWidth={15} stroke={theme.secondary.dark} />
    </CircularInput>
  );
};

export default withTheme(CustomCircularInput);
