import React from 'react';
import OscilloscopeSvg from '../../resources/oscilloscope.svg';
import LogicAnalyserSvg from '../../resources/logic_analyzer.svg';
import PowerSourceSvg from '../../resources/power_source.svg';
import WaveGeneratorSvg from '../../resources/wave_generator.svg';
import MultimeterSvg from '../../resources/multimeter.svg';
import SensorsSvg from '../../resources/sensors.svg';
import OscilloscopeRedSvg from '../../resources/oscilloscope_red.svg';
import LogicAnalyserRedSvg from '../../resources/logic_analyzer_red.svg';
import PowerSourceRedSvg from '../../resources/power_source_red.svg';
import WaveGeneratorRedSvg from '../../resources/wave_generator_red.svg';
import MultimeterRedSvg from '../../resources/multimeter_red.svg';
import SensorsRedSvg from '../../resources/sensors_red.svg';

export const OscilloscopeIcon = ({ size, color }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={color === 'red' ? OscilloscopeRedSvg : OscilloscopeSvg}
    />
  );
};

export const LogicAnalyserIcon = ({ size, color }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={color === 'red' ? LogicAnalyserRedSvg : LogicAnalyserSvg}
    />
  );
};

export const PowerSourceIcon = ({ size, color }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={color === 'red' ? PowerSourceRedSvg : PowerSourceSvg}
    />
  );
};

export const WaveGeneratorIcon = ({ size, color }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={color === 'red' ? WaveGeneratorRedSvg : WaveGeneratorSvg}
    />
  );
};

export const MultimeterIcon = ({ size, color }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={color === 'red' ? MultimeterRedSvg : MultimeterSvg}
    />
  );
};

export const SensorsIcon = ({ size, color }) => {
  return (
    <img
      style={{
        height: size,
        width: 'auto',
      }}
      src={color === 'red' ? SensorsRedSvg : SensorsSvg}
    />
  );
};
