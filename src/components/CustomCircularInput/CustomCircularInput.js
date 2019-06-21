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

const CustomCircularInput = ({
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
          <CircularTrack
            strokeWidth={5}
            stroke={fade(theme.primary.light, 0.5)}
          />
          {!selector && (
            <CircularProgress strokeWidth={15} stroke={theme.primary.main} />
          )}
          {selector && <CircularThumb r={12} fill={theme.primary.dark} />}
        </CircularInput>
      )}
    </Spring>
  );
};

export default withTheme(CustomCircularInput);
