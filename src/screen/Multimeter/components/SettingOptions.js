import React from 'react';
import { TextIcon } from './InstrumentCluster.styles';
import ResistorIcon from '../../../components/CustomIcons/ResistorIcon.js';
import CapacitorIcon from '../../../components/CustomIcons/CapacitorIcon.js';

export const iconMap = (activeSubType, theme) => ({
  CH1: {
    icon: (
      <TextIcon style={{ color: '#d32f2f' }} active={activeSubType === 'CH1'}>
        CH1
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-90deg) translate(160px) rotate(90deg)',
  },
  CH2: {
    icon: (
      <TextIcon style={{ color: '#d32f2f' }} active={activeSubType === 'CH2'}>
        CH2
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-122.72deg) translate(160px) rotate(122.72deg)',
  },
  CH3: {
    icon: (
      <TextIcon style={{ color: '#d32f2f' }} active={activeSubType === 'CH3'}>
        CH3
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-155.44deg) translate(160px) rotate(155.44deg)',
  },
  LA4: {
    icon: (
      <TextIcon style={{ color: '#000' }} active={activeSubType === 'LA4'}>
        LA4
      </TextIcon>
    ),

    transform:
      'translateX(-50%) translateY(-50%) rotate(-188.16deg) translate(160px) rotate(188.16deg)',
  },
  LA3: {
    icon: (
      <TextIcon style={{ color: '#000' }} active={activeSubType === 'LA3'}>
        LA3
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-220.88deg) translate(160px) rotate(220.88deg)',
  },
  LA2: {
    icon: (
      <TextIcon style={{ color: '#000' }} active={activeSubType === 'LA2'}>
        LA2
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-253.6deg) translate(160px) rotate(253.6deg)',
  },
  LA1: {
    icon: (
      <TextIcon style={{ color: '#000' }} active={activeSubType === 'LA1'}>
        LA1
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-286.32deg) translate(160px) rotate(286.32deg)',
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
      'translateX(-50%) translateY(-50%) rotate(-319.04deg) translate(160px) rotate(319.04deg)',
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
      'translateX(-50%) translateY(-50%) rotate(-351.76deg) translate(160px) rotate(351.76deg)',
  },
  VOL: {
    icon: (
      <TextIcon style={{ color: '#d32f2f' }} active={activeSubType === 'VOL'}>
        VOL
      </TextIcon>
    ),
    transform:
      'translateX(-50%) translateY(-50%) rotate(-24.48deg) translate(160px) rotate(24.48deg)',
  },
  CAP: {
    icon: (
      <TextIcon style={{ color: '#d32f2f' }} active={activeSubType === 'CAP'}>
        CAP
      </TextIcon>
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
  'VOL',
  'LA1',
  'LA2',
  'LA3',
  'LA4',
  'RESISTOR',
  'CAPACITOR',
];

export const angleMap = {
  0: 'CH1',
  360: 'CH1',
  327: 'CH2',
  294: 'CH3',
  262: 'LA4',
  229: 'LA3',
  196: 'LA2',
  164: 'LA1',
  131: 'CAPACITOR',
  98: 'RESISTOR',
  65: 'VOL',
  33: 'CAP',
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
  LA4: {
    angle: 262,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  LA3: {
    angle: 229,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  LA2: {
    angle: 196,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  LA1: {
    angle: 164,
    unit: { PULSE_COUNT: '1/sec', PULSE_FREQUENCY: 'Hz' },
    category: 'PULSE',
  },
  CAPACITOR: {
    angle: 131,
    unit: 'F',
    category: 'MISC',
  },
  RESISTOR: {
    angle: 98,
    unit: 'Ω',
    category: 'MISC',
  },
  VOL: {
    angle: 65,
    unit: 'V',
    category: 'VOLTAGE',
  },
  CAP: {
    angle: 33,
    unit: 'V',
    category: 'VOLTAGE',
  },
};
