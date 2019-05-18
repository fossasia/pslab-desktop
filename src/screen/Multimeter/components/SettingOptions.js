import React from 'react';
import { TextIcon } from './InstrumentCluster.styles';
import { IconButton } from '@material-ui/core';
import ResistorIcon from '../../../components/CustomIcons/ResistorIcon.js';
import CapacitorIcon from '../../../components/CustomIcons/CapacitorIcon.js';

export const options = (activeSubType, onClickButton, theme) => ({
  CH1: {
    icon: (
      <IconButton onClick={onClickButton('CH1', 'V', 0)} size="medium">
        <TextIcon active={activeSubType === 'CH1'}>CH1</TextIcon>
      </IconButton>
    ),
    unit: 'V',
    catagory: 'VOLTAGE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-90deg) translate(160px) rotate(90deg)',
  },
  CH2: {
    icon: (
      <IconButton onClick={onClickButton('CH2', 'V', 327)} size="medium">
        <TextIcon active={activeSubType === 'CH2'}>CH2</TextIcon>
      </IconButton>
    ),
    unit: 'V',
    catagory: 'VOLTAGE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-122.72deg) translate(160px) rotate(122.72deg)',
  },
  CH3: {
    icon: (
      <IconButton onClick={onClickButton('CH3', 'V', 294)} size="medium">
        <TextIcon active={activeSubType === 'CH3'}>CH3</TextIcon>
      </IconButton>
    ),
    unit: 'V',
    catagory: 'VOLTAGE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-155.44deg) translate(160px) rotate(155.44deg)',
  },
  CAP: {
    icon: (
      <IconButton onClick={onClickButton('CAP', 'V', 262)} size="medium">
        <TextIcon active={activeSubType === 'CAP'}>CAP</TextIcon>
      </IconButton>
    ),
    unit: 'V',
    catagory: 'VOLTAGE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-188.16deg) translate(160px) rotate(188.16deg)',
  },
  AN8: {
    icon: (
      <IconButton onClick={onClickButton('AN8', 'V', 229)} size="medium">
        <TextIcon active={activeSubType === 'AN8'}>AN8</TextIcon>
      </IconButton>
    ),
    unit: 'V',
    catagory: 'VOLTAGE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-220.88deg) translate(160px) rotate(220.88deg)',
  },
  ID1: {
    icon: (
      <IconButton onClick={onClickButton('ID1', 'Hz', 196)} size="medium">
        <TextIcon active={activeSubType === 'ID1'}>ID1</TextIcon>
      </IconButton>
    ),
    unit: 'Hz',
    catagory: 'PULSE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-253.6deg) translate(160px) rotate(253.6deg)',
  },
  ID2: {
    icon: (
      <IconButton onClick={onClickButton('ID2', 'Hz', 164)} size="medium">
        <TextIcon active={activeSubType === 'ID2'}>ID2</TextIcon>
      </IconButton>
    ),
    unit: 'Hz',
    catagory: 'PULSE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-286.32deg) translate(160px) rotate(286.32deg)',
  },
  ID3: {
    icon: (
      <IconButton onClick={onClickButton('ID3', 'Hz', 131)} size="medium">
        <TextIcon active={activeSubType === 'ID3'}>ID3</TextIcon>
      </IconButton>
    ),
    unit: 'Hz',
    catagory: 'PULSE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-319.04deg) translate(160px) rotate(319.04deg)',
  },
  ID4: {
    icon: (
      <IconButton onClick={onClickButton('ID4', 'Hz', 98)} size="medium">
        <TextIcon active={activeSubType === 'ID4'}>ID4</TextIcon>
      </IconButton>
    ),
    unit: 'Hz',
    catagory: 'PULSE',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-351.76deg) translate(160px) rotate(351.76deg)',
  },
  RESISTOR: {
    icon: (
      <IconButton onClick={onClickButton('RESISTOR', 'Ω', 65)} size="medium">
        <ResistorIcon
          color={
            activeSubType === 'RESISTOR'
              ? theme.secondary.dark
              : theme.text.hint
          }
          size="34px"
        />
      </IconButton>
    ),
    unit: 'Ω',
    catagory: 'MISC',
    transform:
      'translateX(-50%) translateY(-50%) rotate(-24.48deg) translate(160px) rotate(24.48deg)',
  },
  CAPACITOR: {
    icon: (
      <IconButton onClick={onClickButton('CAPACITOR', 'pF', 33)} size="medium">
        <CapacitorIcon
          color={
            activeSubType === 'CAPACITOR'
              ? theme.secondary.dark
              : theme.text.hint
          }
          size={'34px'}
        />
      </IconButton>
    ),
    unit: 'pF',
    catagory: 'MISC',
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
