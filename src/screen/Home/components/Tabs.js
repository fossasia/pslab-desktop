import React from 'react';
import { Scrollbars } from 'react-custom-scrollbars';
import InstrumentCard from './InstrumentCard';
import { TabsContainer, TabsContainerInner } from './Tabs.styles';
import {
  OscilloscopeIcon,
  LogicAnalyzerIcon,
  WaveGeneratorIcon,
  PowerSourceIcon,
  MultimeterIcon,
  SensorsIcon,
} from '../../../components/Icons/PSLabIcons';

const Tabs = () => {
  return (
    <Scrollbars autoHide autoHideTimeout={1000}>
      <TabsContainer>
        <TabsContainerInner>
          <InstrumentCard
            icon={<OscilloscopeIcon size={'10em'} />}
            title={'Oscilloscope'}
            description={'Allows observation of varying signal voltages'}
            redirectPath={'/oscilloscope'}
          />
          <InstrumentCard
            icon={<LogicAnalyzerIcon size={'10em'} />}
            title={'Logic Analyzer'}
            description={'Captures and displays signals from digital systems'}
            redirectPath={'/logicanalyzer'}
          />
          <InstrumentCard
            icon={<WaveGeneratorIcon size={'10em'} />}
            title={'Wave Generator'}
            description={'Generates arbitrary analog and digital waveforms'}
            redirectPath={'/wavegenerator'}
          />
          <InstrumentCard
            icon={<PowerSourceIcon size={'10em'} />}
            title={'Power Source'}
            description={'Generates programmable voltage and currents'}
            redirectPath={'/powersource'}
          />
          <InstrumentCard
            icon={<MultimeterIcon size={'10em'} />}
            title={'Multimeter'}
            description={
              'Measure voltage, current, resistance and capacitance.'
            }
            redirectPath={'/multimeter'}
          />
          <InstrumentCard
            icon={<SensorsIcon size={'10em'} />}
            title={'Sensors'}
            description={'Allows logging of data returned by sensor connected.'}
            redirectPath={'/sensors'}
          />
          <InstrumentCard
            icon={<MultimeterIcon size={'10em'} />}
            title={'Robotic Arm'}
            description={'To control servo motors using a timeline.'}
            redirectPath={'/robotarm'}
          />
        </TabsContainerInner>
      </TabsContainer>
    </Scrollbars>
  );
};

export default Tabs;
