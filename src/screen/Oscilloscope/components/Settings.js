import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import { SettingsContainer } from './Settings.styles';
import ChannelParameters from './ChannelParameters';
import TimeParameters from './TimeParameters';
import AnalysisParameters from './AnalysisParameters';
import PlotParameters from './PlotParameters';

const Settings = ({
  activeChannels,
  channelRanges,
  channelMaps,
  onToggleChannel,
  onChangeChannelRange,
  onChangeChannelMap,
  onChangeTriggerVoltage,
  onChangeTriggerChannel,
  onChangeTimeBaseIndex,
  triggerVoltage,
  timeBaseListLength,
  timeBaseIndex,
  timeBase,
  triggerVoltageChannel,
  isTriggerActive,
  isFourierTransformActive,
  transformType,
  transformChannel1,
  transformChannel2,
  onChangeTransformType,
  onChangeTransformChannel,
  isXYPlotActive,
  plotChannel1,
  plotChannel2,
  onChangePlotChannel,
  isMicActive,
  onToggleCheckBox,
}) => (
  <SettingsContainer>
    <Scrollbars autoHide autoHideTimeout={1000}>
      <ChannelParameters
        onToggleCheckBox={onToggleCheckBox}
        isMicActive={isMicActive}
        activeChannels={activeChannels}
        channelRanges={channelRanges}
        channelMaps={channelMaps}
        onToggleChannel={onToggleChannel}
        onChangeChannelRange={onChangeChannelRange}
        onChangeChannelMap={onChangeChannelMap}
      />
      <TimeParameters
        onChangeTriggerVoltage={onChangeTriggerVoltage}
        onChangeTriggerChannel={onChangeTriggerChannel}
        onChangeTimeBaseIndex={onChangeTimeBaseIndex}
        triggerVoltage={triggerVoltage}
        timeBaseListLength={timeBaseListLength}
        timeBaseIndex={timeBaseIndex}
        timeBase={timeBase}
        triggerVoltageChannel={triggerVoltageChannel}
        isTriggerActive={isTriggerActive}
        onToggleCheckBox={onToggleCheckBox}
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
        onToggleCheckBox={onToggleCheckBox}
        plotChannel1={plotChannel1}
        plotChannel2={plotChannel2}
        onChangePlotChannel={onChangePlotChannel}
      />
    </Scrollbars>
  </SettingsContainer>
);

export default Settings;
