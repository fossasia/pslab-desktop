import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import { SettingsContainer } from './Settings.styles';
import ChannelParameters from './ChannelParameters';
import TimeParameters from './TimeParameters';
import { options } from './settingOptions';

const Settings = ({
  activeChannels,
  channelRanges,
  channelMaps,
  triggerChannel,
  onToggleChannel,
  onChangeChannelRange,
  onChangeChannelMap,
  onChangeTriggerChannel,
  onChangeID,
  channelID,
  edgeSelection,
  onEdgeChange,
}) => (
  <SettingsContainer>
    <Scrollbars autoHide autoHideTimeout={1000}>  
      <ChannelParameters
        activeChannels={activeChannels}
        channelRanges={channelRanges}
        channelMaps={channelMaps}
        triggerChannel={triggerChannel}
        onToggleChannel={onToggleChannel}
        onChangeChannelRange={onChangeChannelRange}
        onChangeChannelMap={onChangeChannelMap}
        onChangeTriggerChannel={onChangeTriggerChannel}
      />
      <TimeParameters
        channelID={channelID}
        edgeSelection={edgeSelection}
        onEdgeChange={onEdgeChange}
        onChangeID={onChangeID}
      />
         <TimeParameters
        channelID={channelID}
        edgeSelection={edgeSelection}
        onEdgeChange={onEdgeChange}
        onChangeID={onChangeID}
        disabled={triggerChannel == options.Select.CH1}
      />
         <TimeParameters
        channelID={channelID}
        edgeSelection={edgeSelection}
        onEdgeChange={onEdgeChange}
        onChangeID={onChangeID}
        disabled={triggerChannel == options.Select.CH1 || triggerChannel == options.Select.CH2}
      />
         <TimeParameters
        channelID={channelID}
        edgeSelection={edgeSelection}
        onEdgeChange={onEdgeChange}
        onChangeID={onChangeID}
        disabled={triggerChannel == options.Select.CH1 || triggerChannel == options.Select.CH2 || triggerChannel == options.Select.CH3 }
      />
    </Scrollbars>
  </SettingsContainer>
  
);

export default Settings;
