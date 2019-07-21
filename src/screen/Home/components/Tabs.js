import React from 'react';
import { Settings as SettingIcon, TabRounded } from '@material-ui/icons';
import { Scrollbars } from 'react-custom-scrollbars';
import InstrumentCard from './InstrumentCard';
import { TabsContainer, TabsWrapper, TabsRow } from './Tabs.styles';
import {
  OscilloscopeIcon,
  LogicAnalyserIcon,
  WaveGeneratorIcon,
  PowerSourceIcon,
  MultimeterIcon,
  SensorsIcon,
} from '../../../components/Icons/PSLabIcons';

const Tabs = () => {
  return (
    <TabsContainer>
      <Scrollbars autoHide autoHideTimeout={1000}>
        <TabsRow>
          <TabsWrapper>
            <InstrumentCard
              icon={<OscilloscopeIcon size={'10em'} />}
              title={'Oscilloscope'}
              description={'Allows observation of varying signal voltages'}
              redirectPath={'/oscilloscope'}
            />
          </TabsWrapper>
          <TabsWrapper>
            <InstrumentCard
              icon={<LogicAnalyserIcon size={'10em'} />}
              title={'Logic Analyser'}
              description={'Captures and displays signals from digital systems'}
              redirectPath={'/logicanalyser'}
            />
          </TabsWrapper>
        </TabsRow>
        <TabsRow>
          <TabsWrapper>
            <InstrumentCard
              icon={<WaveGeneratorIcon size={'10em'} />}
              title={'Wave Generator'}
              description={'Generates arbitrary analog and digital waveforms'}
              redirectPath={'/wavegenerator'}
            />
          </TabsWrapper>
          <TabsWrapper>
            <InstrumentCard
              icon={<PowerSourceIcon size={'10em'} />}
              title={'Power Source'}
              description={'Generates programmable voltage and currents'}
              redirectPath={'/powersource'}
            />
          </TabsWrapper>
        </TabsRow>
        <TabsRow>
          <TabsWrapper>
            <InstrumentCard
              icon={<MultimeterIcon size={'10em'} />}
              title={'Multimeter'}
              description={
                'Measure voltage, current, resistance and capacitance.'
              }
              redirectPath={'/multimeter'}
            />
          </TabsWrapper>
          <TabsWrapper>
            <InstrumentCard
              icon={<SensorsIcon size={'10em'} />}
              title={'Sensors'}
              description={
                'Allows logging of data returned by sensor connected.'
              }
              redirectPath={'/sensors'}
            />
          </TabsWrapper>
        </TabsRow>
        <TabsRow>
          <TabsWrapper>
            <InstrumentCard
              icon={<MultimeterIcon size={'10em'} />}
              title={'Robotic Arm'}
              description={'To control servo motors using a timeline.'}
              redirectPath={'/robotarm'}
            />
          </TabsWrapper>
        </TabsRow>
      </Scrollbars>
    </TabsContainer>
  );
};

export default Tabs;
