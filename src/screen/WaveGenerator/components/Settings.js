import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import { SettingsContainer } from './Settings.styles';
import SineWaveParameters from './SineWaveParameters';
import SquareWaveParameters from './SquareWaveParameters';

const Settings = ({
  wave,
  digital,
  s1Frequency,
  s2Frequency,
  s2Phase,
  pwmFrequency,
  sqr1DutyCycle,
  sqr2DutyCycle,
  sqr2Phase,
  sqr3DutyCycle,
  sqr3Phase,
  sqr4DutyCycle,
  sqr4Phase,
  waveFormS1,
  waveFormS2,
  onTogglePreview,
  onChangeWaveForm,
  onChangeSlider,
}) => (
  <SettingsContainer>
    <Scrollbars autoHide autoHideTimeout={1000}>
      <SineWaveParameters
        wave={wave}
        s1Frequency={s1Frequency}
        s2Frequency={s2Frequency}
        s2Phase={s2Phase}
        waveFormS1={waveFormS1}
        waveFormS2={waveFormS2}
        onTogglePreview={onTogglePreview}
        onChangeWaveForm={onChangeWaveForm}
        onChangeSlider={onChangeSlider}
      />
      <SquareWaveParameters
        digital={digital}
        pwmFrequency={pwmFrequency}
        sqr1DutyCycle={sqr1DutyCycle}
        sqr2DutyCycle={sqr2DutyCycle}
        sqr2Phase={sqr2Phase}
        sqr3DutyCycle={sqr3DutyCycle}
        sqr3Phase={sqr3Phase}
        sqr4DutyCycle={sqr4DutyCycle}
        sqr4Phase={sqr4Phase}
        onTogglePreview={onTogglePreview}
        onChangeSlider={onChangeSlider}
      />
    </Scrollbars>
  </SettingsContainer>
);

export default Settings;
