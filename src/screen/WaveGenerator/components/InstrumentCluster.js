import React from 'react';
import SineWavePanel from './SineWavePanel';
import SquareWavePanel from './SquareWavePanel';
import { SettingsContainer } from './InstrumentCluster.styles';

const InstrumentCluster = () => {
  return (
    <SettingsContainer>
      <div>
        <SineWavePanel />
      </div>
      <div>
        <SquareWavePanel />
      </div>
    </SettingsContainer>
  );
};

export default InstrumentCluster;
