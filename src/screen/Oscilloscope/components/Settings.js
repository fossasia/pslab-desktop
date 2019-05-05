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
  onToggleTrigger,
  onChangeTriggerVoltage,
  onChangeTriggerChannel,
  onChangeTimeBase,
  triggerVoltage,
  timeBase,
  triggerVoltageChannel,
  isTriggerActive,
  isFourierTransformActive,
  transformType,
  transformChannel1,
  transformChannel2,
  onTOggleFourierTransform,
  onChangeTransformType,
  onChangeTransformChannel,
  isXYPlotActive,
  plotChannel1,
  plotChannel2,
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
        onToggleTrigger={onToggleTrigger}
        onChangeTriggerVoltage={onChangeTriggerVoltage}
        onChangeTriggerChannel={onChangeTriggerChannel}
        onChangeTimeBase={onChangeTimeBase}
        triggerVoltage={triggerVoltage}
        timeBase={timeBase}
        triggerVoltageChannel={triggerVoltageChannel}
        isTriggerActive={isTriggerActive}
      />
      <AnalysisParameters
        isFourierTransformActive={isFourierTransformActive}
        transformType={transformType}
        transformChannel1={transformChannel1}
        transformChannel2={transformChannel2}
        onTOggleFourierTransform={onTOggleFourierTransform}
        onChangeTransformType={onChangeTransformType}
        onChangeTransformChannel={onChangeTransformChannel}
      />
      <PlotParameters
        isXYPlotActive={isXYPlotActive}
        plotChannel1={plotChannel1}
        plotChannel2={plotChannel2}
        onChangePlotChannel={onChangePlotChannel}
      />
    </Scrollbars>
  </SettingsContainer>
);

export default Settings;
