import React from 'react';
import { ValueWrapper } from './Display.styles';

const Display = ({ fontSize, value, unit }) => (
  <ValueWrapper fontSize={fontSize}>
    {value} {unit}
  </ValueWrapper>
);

export default Display;
