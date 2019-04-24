import React from 'react';
import { ValueContainer, ValueWrapper } from './Display.styles';

const Display = props => {
  const { value, unit } = props;

  return (
    <ValueContainer>
      <ValueWrapper>
        {value} {unit}
      </ValueWrapper>
    </ValueContainer>
  );
};

export default Display;
