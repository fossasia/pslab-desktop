import React from 'react';
import s3 from './skins/s3';
import { Knob } from 'react-rotary-knob';

const CustomKnob = ({ radius, onChangeDial, value, step, min, max }) => {
  return (
    <Knob
      style={{
        display: 'inline-block',
        width: `${radius}em`,
        height: `${radius}em`,
      }}
      value={value}
      step={step}
      min={min}
      max={max}
      preciseMode={false}
      onChange={onChangeDial}
      skin={s3}
    />
  );
};

export default CustomKnob;
