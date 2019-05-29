import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import { SettingsContainer } from './Settings.styles';
import SineWaveParameters from './SineWaveParameters';
import SquareWaveParameters from './SquareWaveParameters';

const Settings = ({
  activePreview,
  s1Frequency,
  s2Frequency,
  s2Phase,
  sqr1Frequency,
  sqr1DutyCycle,
  sqr2Frequency,
  sqr2DutyCycle,
  sqr2Phase,
  sqr3Frequency,
  sqr3DutyCycle,
  sqr3Phase,
  sqr4Frequency,
  sqr4DutyCycle,
  sqr4Phase,
  waveFormS1,
  waveFormS2,
  mode,
  onTogglePreview,
  onChangeWaveForm,
  onChangeMode,
  onChangeSlider,
}) => (
  <SettingsContainer>
    <Scrollbars autoHide autoHideTimeout={1000}>
      <SineWaveParameters
        activePreview={activePreview}
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
        activePreview={activePreview}
        mode={mode}
        sqr1Frequency={sqr1Frequency}
        sqr1DutyCycle={sqr1DutyCycle}
        sqr2Frequency={sqr2Frequency}
        sqr2DutyCycle={sqr2DutyCycle}
        sqr2Phase={sqr2Phase}
        sqr3Frequency={sqr3Frequency}
        sqr3DutyCycle={sqr3DutyCycle}
        sqr3Phase={sqr3Phase}
        sqr4Frequency={sqr4Frequency}
        sqr4DutyCycle={sqr4DutyCycle}
        sqr4Phase={sqr4Phase}
        onTogglePreview={onTogglePreview}
        onChangeMode={onChangeMode}
        onChangeSlider={onChangeSlider}
      />
    </Scrollbars>
  </SettingsContainer>
);

export default Settings;
