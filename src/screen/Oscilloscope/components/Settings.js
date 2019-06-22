import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import {
  SettingsContainer,
  FixedWrapper,
  ScrollWrapper,
} from './Settings.styles';
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
  fitType,
  fitChannel1,
  fitChannel2,
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
  onChangeFitType,
  onChangeFitChannel,
  onChangePlotChannel,
}) => (
  <SettingsContainer>
    <FixedWrapper>
      <ChannelParameters
        activeChannels={activeChannels}
        channelRanges={channelRanges}
        channelMaps={channelMaps}
        onToggleChannel={onToggleChannel}
        onChangeChannelRange={onChangeChannelRange}
        onChangeChannelMap={onChangeChannelMap}
      />
    </FixedWrapper>
    <ScrollWrapper>
      <Scrollbars autoHide autoHideTimeout={1000}>
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
          fitType={fitType}
          fitChannel1={fitChannel1}
          fitChannel2={fitChannel2}
          onToggleCheckBox={onToggleCheckBox}
          onChangeFitType={onChangeFitType}
          onChangeFitChannel={onChangeFitChannel}
        />
        <PlotParameters
          isXYPlotActive={isXYPlotActive}
          plotChannel1={plotChannel1}
          plotChannel2={plotChannel2}
          onToggleCheckBox={onToggleCheckBox}
          onChangePlotChannel={onChangePlotChannel}
        />
      </Scrollbars>
    </ScrollWrapper>
  </SettingsContainer>
);

export default Settings;
