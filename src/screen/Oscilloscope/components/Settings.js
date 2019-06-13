import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import { SettingsContainer } from './Settings.styles';
import ChannelParameters from './ChannelParameters';
import TimeParameters from './TimeParameters';
import AnalysisParameters from './AnalysisParameters';
import PlotParameters from './PlotParameters';

const Settings = () => (
  <SettingsContainer>
    <Scrollbars autoHide autoHideTimeout={1000}>
      <ChannelParameters />
      <TimeParameters />
      <AnalysisParameters />
      <PlotParameters />
    </Scrollbars>
  </SettingsContainer>
);

export default Settings;
