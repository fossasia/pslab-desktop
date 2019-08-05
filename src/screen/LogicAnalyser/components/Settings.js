import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import {
  SettingsContainer,
  FixedWrapper,
  ScrollWrapper,
} from './Settings.styles';
import NumberParameter from './NumberParameter';
import ChannelParameters from './ChannelParameters';
import AnalysisParameters from './AnalysisParameters';

const Settings = ({
  numberOfChannels,
  channel1Map,
  channel2Map,
  trigger1Type,
  trigger2Type,
  trigger3Type,
  trigger4Type,
  timeMeasureChannel1,
  timeMeasureChannel2,
  timeMeasuretrigger1Type,
  timeMeasuretrigger2Type,
  timeMeasureWrite1,
  timeMeasureWrite2,
  timeout,
  changeNumberOfChannels,
  changeChannelMap,
  changeTriggerType,
  changeTimeMeasureChannel,
  changeTimeMeasureTriggerType,
  changeTimeMeasureWrite,
  changeTimeout,
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
        {/* <AnalysisParameters
          timeMeasureChannel1={timeMeasureChannel1}
          timeMeasureChannel2={timeMeasureChannel2}
          timeMeasuretrigger1Type={timeMeasuretrigger1Type}
          timeMeasuretrigger2Type={timeMeasuretrigger2Type}
          timeMeasureWrite1={timeMeasureWrite1}
          timeMeasureWrite2={timeMeasureWrite2}
          timeout={timeout}
          changeTimeMeasureChannel={changeTimeMeasureChannel}
          changeTimeMeasureTriggerType={changeTimeMeasureTriggerType}
          changeTimeMeasureWrite={changeTimeMeasureWrite}
          changeTimeout={changeTimeout}
        /> */}
      </Scrollbars>
    </ScrollWrapper>
  </SettingsContainer>
);

export default Settings;
