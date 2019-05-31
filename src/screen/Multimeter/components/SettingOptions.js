import React from 'react';
import { TextIcon } from './InstrumentCluster.styles';
import ResistorIcon from '../../../components/CustomIcons/ResistorIcon.js';
import CapacitorIcon from '../../../components/CustomIcons/CapacitorIcon.js';

export const iconMap = (activeSubType, theme) => ({
  CH1: {
    icon: <TextIcon active={activeSubType === 'CH1'}>CH1</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-90deg) translate(160px) rotate(90deg)',
  },
  CH2: {
    icon: <TextIcon active={activeSubType === 'CH2'}>CH2</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-122.72deg) translate(160px) rotate(122.72deg)',
  },
  CH3: {
    icon: <TextIcon active={activeSubType === 'CH3'}>CH3</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-155.44deg) translate(160px) rotate(155.44deg)',
  },
  CAP: {
    icon: <TextIcon active={activeSubType === 'CAP'}>CAP</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-188.16deg) translate(160px) rotate(188.16deg)',
  },
  AN8: {
    icon: <TextIcon active={activeSubType === 'AN8'}>AN8</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-220.88deg) translate(160px) rotate(220.88deg)',
  },
  ID1: {
    icon: <TextIcon active={activeSubType === 'ID1'}>ID1</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-253.6deg) translate(160px) rotate(253.6deg)',
  },
  ID2: {
    icon: <TextIcon active={activeSubType === 'ID2'}>ID2</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-286.32deg) translate(160px) rotate(286.32deg)',
  },
  ID3: {
    icon: <TextIcon active={activeSubType === 'ID3'}>ID3</TextIcon>,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-319.04deg) translate(160px) rotate(319.04deg)',
  },
  ID4: {
    icon: <TextIcon active={activeSubType === 'ID4'}>ID4</TextIcon>,

    transform:
      'translateX(-50%) translateY(-50%) rotate(-351.76deg) translate(160px) rotate(351.76deg)',
  },
  RESISTOR: {
    icon: (
      <ResistorIcon
        color={
          activeSubType === 'RESISTOR' ? theme.secondary.dark : theme.text.hint
        }
        size="34px"
      />
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-24.48deg) translate(160px) rotate(24.48deg)',
  },
  CAPACITOR: {
    icon: (
      <CapacitorIcon
        color={
          activeSubType === 'CAPACITOR' ? theme.secondary.dark : theme.text.hint
        }
        size={'34px'}
      />
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-57.2deg) translate(160px) rotate(57.2deg)',
  },
});

export const optionsOrder = [
  'CH1',
  'CH2',
  'CH3',
  'CAP',
  'AN8',
  'ID1',
  'ID2',
  'ID3',
  'ID4',
  'RESISTOR',
  'CAPACITOR',
];

export const angleMap = {
  0: 'CH1',
  360: 'CH1',
  33: 'CAPACITOR',
  65: 'RESISTOR',
  98: 'ID4',
  131: 'ID3',
  164: 'ID2',
  196: 'ID1',
  229: 'AN8',
  262: 'CAP',
  294: 'CH3',
  327: 'CH2',
};

export const optionMap = {
  CH1: {
    angle: 0,
    unit: 'V',
    category: 'VOLTAGE',
  },
  CH2: {
    angle: 327,
    unit: 'V',
    category: 'VOLTAGE',
  },
  CH3: {
    angle: 294,
    unit: 'V',
    category: 'VOLTAGE',
  },
  CAP: {
    angle: 262,
    unit: 'V',
    category: 'VOLTAGE',
  },
  AN8: {
    angle: 229,
    unit: 'V',
    category: 'VOLTAGE',
  },
  ID1: {
    angle: 196,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  ID2: {
    angle: 164,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  ID3: {
    angle: 131,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  ID4: {
    angle: 98,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  RESISTOR: {
    angle: 65,
    unit: 'Ω',
    category: 'MISC',
  },
  CAPACITOR: {
    angle: 33,
    unit: 'F',
    category: 'MISC',
  },
};
