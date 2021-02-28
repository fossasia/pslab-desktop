import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import {
  SettingsContainer,
  FixedWrapper,
  ScrollWrapper,
} from './Settings.styles';
import NumberParameter from './NumberParameter';
import ChannelParameters from './ChannelParameters';
import TimeParameters from './TimeParameters';
const Settings = ({
  numberOfChannels,
  channel1Map,
  channel2Map,
  trigger1Type,
  trigger2Type,
  trigger3Type,
  trigger4Type,
  changeNumberOfChannels,
  changeChannelMap,
  changeTriggerType,
  onChangeCaptureTime,
  captureTime,
  maxCaptureTime,
}) => (
  <SettingsContainer>
    <FixedWrapper>
      <NumberParameter
        numberOfChannels={numberOfChannels}
        changeNumberOfChannels={changeNumberOfChannels}
      />
    </FixedWrapper>
    <ScrollWrapper>
      <Scrollbars autoHide autoHideTimeout={1000}>
        <ChannelParameters
          numberOfChannels={numberOfChannels}
          channel1Map={channel1Map}
          channel2Map={channel2Map}
          trigger1Type={trigger1Type}
          trigger2Type={trigger2Type}
          trigger3Type={trigger3Type}
          trigger4Type={trigger4Type}
          changeChannelMap={changeChannelMap}
          changeTriggerType={changeTriggerType}
        />
        <TimeParameters
          onChangeCaptureTime={onChangeCaptureTime}
          captureTime={captureTime}
          maxCaptureTime={maxCaptureTime}
        />
      </Scrollbars>
    </ScrollWrapper>
  </SettingsContainer>
);

export default Settings;
