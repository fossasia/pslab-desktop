import React from 'react';
import OscilloscopeSvg from '../../resources/oscilloscope.svg';
import LogicAnalyserSvg from '../../resources/logic_analyzer.svg';
import PowerSourceSvg from '../../resources/power_source.svg';
import WaveGeneratorSvg from '../../resources/wave_generator.svg';
import MultimeterSvg from '../../resources/multimeter.svg';

export const OscilloscopeIcon = ({ size }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={OscilloscopeSvg}
    />
  );
};

export const LogicAnalyserIcon = ({ size }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={LogicAnalyserSvg}
    />
  );
};

export const PowerSourceIcon = ({ size }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={PowerSourceSvg}
    />
  );
};

export const WaveGeneratorIcon = ({ size }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={WaveGeneratorSvg}
    />
  );
};

export const MultimeterIcon = ({ size }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={MultimeterSvg}
    />
  );
};
