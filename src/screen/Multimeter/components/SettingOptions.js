import React from 'react';
import { TextIcon } from './InstrumentCluster.styles';
import ResistorIcon from '../../../components/CustomIcons/ResistorIcon.js';
import CapacitorIcon from '../../../components/CustomIcons/CapacitorIcon.js';

export const options = (activeSubType, parameter, theme) => ({
  CH1: {
    icon: <TextIcon active={activeSubType === 'CH1'}>CH1</TextIcon>,
    unit: 'V',
    category: 'VOLTAGE',
    dialValue: 0,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-90deg) translate(160px) rotate(90deg)',
  },
  CH2: {
    icon: <TextIcon active={activeSubType === 'CH2'}>CH2</TextIcon>,
    unit: 'V',
    category: 'VOLTAGE',
    dialValue: 327,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-122.72deg) translate(160px) rotate(122.72deg)',
  },
  CH3: {
    icon: <TextIcon active={activeSubType === 'CH3'}>CH3</TextIcon>,
    unit: 'V',
    category: 'VOLTAGE',
    dialValue: 294,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-155.44deg) translate(160px) rotate(155.44deg)',
  },
  CAP: {
    icon: <TextIcon active={activeSubType === 'CAP'}>CAP</TextIcon>,
    unit: 'V',
    category: 'VOLTAGE',
    dialValue: 262,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-188.16deg) translate(160px) rotate(188.16deg)',
  },
  AN8: {
    icon: <TextIcon active={activeSubType === 'AN8'}>AN8</TextIcon>,
    unit: 'V',
    category: 'VOLTAGE',
    dialValue: 229,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-220.88deg) translate(160px) rotate(220.88deg)',
  },
  ID1: {
    icon: <TextIcon active={activeSubType === 'ID1'}>ID1</TextIcon>,
    unit:
      parameter === 'PULSE_FREQUENCY'
        ? 'Hz'
        : parameter === 'PULSE_COUNT'
        ? 'xyz'
        : 'Hz',
    category: 'PULSE',
    dialValue: 196,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-253.6deg) translate(160px) rotate(253.6deg)',
    parameter:
      parameter === null || parameter === undefined
        ? 'PULSE_FREQUENCY'
        : parameter,
  },
  ID2: {
    icon: <TextIcon active={activeSubType === 'ID2'}>ID2</TextIcon>,
    unit:
      parameter === 'PULSE_FREQUENCY'
        ? 'Hz'
        : parameter === 'PULSE_COUNT'
        ? 'xyz'
        : 'Hz',
    category: 'PULSE',
    dialValue: 164,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-286.32deg) translate(160px) rotate(286.32deg)',
    parameter:
      parameter === null || parameter === undefined
        ? 'PULSE_FREQUENCY'
        : parameter,
  },
  ID3: {
    icon: <TextIcon active={activeSubType === 'ID3'}>ID3</TextIcon>,
    unit:
      parameter === 'PULSE_FREQUENCY'
        ? 'Hz'
        : parameter === 'PULSE_COUNT'
        ? 'xyz'
        : 'Hz',
    category: 'PULSE',
    dialValue: 131,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-319.04deg) translate(160px) rotate(319.04deg)',
    parameter:
      parameter === null || parameter === undefined
        ? 'PULSE_FREQUENCY'
        : parameter,
  },
  ID4: {
    icon: <TextIcon active={activeSubType === 'ID4'}>ID4</TextIcon>,
    unit:
      parameter === 'PULSE_FREQUENCY'
        ? 'Hz'
        : parameter === 'PULSE_COUNT'
        ? 'xyz'
        : 'Hz',
    category: 'PULSE',
    dialValue: 98,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-351.76deg) translate(160px) rotate(351.76deg)',
    parameter:
      parameter === null || parameter === undefined
        ? 'PULSE_FREQUENCY'
        : parameter,
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
    unit: 'Ω',
    category: 'MISC',
    dialValue: 65,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-24.48deg) translate(160px) rotate(24.48deg)',
    parameter: null,
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
    unit: 'pF',
    category: 'MISC',
    dialValue: 33,
    transform:
      'translateX(-50%) translateY(-50%) rotate(-57.2deg) translate(160px) rotate(57.2deg)',
  },
  parameter: null,
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
