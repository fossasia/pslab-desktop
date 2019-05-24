import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import { SettingsContainer } from './Settings.styles';
import ChannelParameters from './ChannelParameters';
import TimeParameters from './TimeParameters';
import AnalysisParameters from './AnalysisParameters';
import PlotParameters from './PlotParameters';

const Settings = ({
  timeBaseIndex,
  timeBase,
  activeChannels,
  channelRanges,
  isTriggerActive,
  channelMaps,
  triggerVoltage,
  triggerChannel,
  isFourierTransformActive,
  transformType,
  transformChannel1,
  transformChannel2,
  isXYPlotActive,
  plotChannel1,
  plotChannel2,
  onToggleChannel,
  onChangeChannelRange,
  onChangeChannelMap,
  onToggleCheckBox,
  onChangeTriggerVoltage,
  onChangeTriggerChannel,
  onChangeTimeBaseIndex,
  timeBaseListLength,
  onChangeTransformType,
  onChangeTransformChannel,
  onChangePlotChannel,
}) => (
  <SettingsContainer>
    <Scrollbars autoHide autoHideTimeout={1000}>
      <ChannelParameters
        activeChannels={activeChannels}
        channelRanges={channelRanges}
        channelMaps={channelMaps}
        onToggleChannel={onToggleChannel}
        onChangeChannelRange={onChangeChannelRange}
        onChangeChannelMap={onChangeChannelMap}
      />
      <TimeParameters
        triggerVoltage={triggerVoltage}
        timeBaseListLength={timeBaseListLength}
        timeBaseIndex={timeBaseIndex}
        timeBase={timeBase}
        triggerChannel={triggerChannel}
        isTriggerActive={isTriggerActive}
        onToggleCheckBox={onToggleCheckBox}
        onChangeTriggerVoltage={onChangeTriggerVoltage}
        onChangeTriggerChannel={onChangeTriggerChannel}
        onChangeTimeBaseIndex={onChangeTimeBaseIndex}
      />
      <AnalysisParameters
        isFourierTransformActive={isFourierTransformActive}
        transformType={transformType}
        transformChannel1={transformChannel1}
        transformChannel2={transformChannel2}
        onToggleCheckBox={onToggleCheckBox}
        onChangeTransformType={onChangeTransformType}
        onChangeTransformChannel={onChangeTransformChannel}
      />
      <PlotParameters
        isXYPlotActive={isXYPlotActive}
        plotChannel1={plotChannel1}
        plotChannel2={plotChannel2}
        onToggleCheckBox={onToggleCheckBox}
        onChangePlotChannel={onChangePlotChannel}
      />
    </Scrollbars>
  </SettingsContainer>
);

export default Settings;
