import React from 'react';
import { Card } from '@material-ui/core';
import {
  InstrumentContainer,
  DisplayContainer,
  DisplayWrapper,
  TextIcon,
  ImageIcon,
} from './InstrumentCluster.styles';
import LinearProgress from '@material-ui/core/LinearProgress';
import { IconButton } from '@material-ui/core';
import ResistorIcon from '../../../resources/ResistorIcon.js';
import CapacitorIcon from '../../../resources/CapacitorIcon.js';
import Dial from './Dial';
import Display from '../../../components/Display';
import ActionButtons from './ActionButtons';
import { withTheme, withStyles } from '@material-ui/core/styles';

const styles = () => ({
  cardMargin: {
    margin: '0px 16px 0px 0px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
  },
});

const InstrumentCluster = ({
  activeOption,
  onClickButton,
  onChangeDial,
  dialValue,
  data,
  unit,
  theme,
  classes,
}) => {
  const options = [
    {
      icon: (
        <IconButton onClick={onClickButton('CH1', 'V', 0)} size="medium">
          <TextIcon active={activeOption === 'CH1'}>CH1</TextIcon>
        </IconButton>
      ),
      name: 'CH1',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-90deg) translate(160px) rotate(90deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('CH2', 'V', 327)} size="medium">
          <TextIcon active={activeOption === 'CH2'}>CH2</TextIcon>
        </IconButton>
      ),
      name: 'CH2',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-122.72deg) translate(160px) rotate(122.72deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('CH3', 'V', 294)} size="medium">
          <TextIcon active={activeOption === 'CH3'}>CH3</TextIcon>
        </IconButton>
      ),
      name: 'CH3',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-155.44deg) translate(160px) rotate(155.44deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('CAP', 'V', 262)} size="medium">
          <TextIcon active={activeOption === 'CAP'}>CAP</TextIcon>
        </IconButton>
      ),
      name: 'CAP',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-188.16deg) translate(160px) rotate(188.16deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('AN8', 'V', 229)} size="medium">
          <TextIcon active={activeOption === 'AN8'}>AN8</TextIcon>
        </IconButton>
      ),
      name: 'AN8',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-220.88deg) translate(160px) rotate(220.88deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('ID1', 'Hz', 196)} size="medium">
          <TextIcon active={activeOption === 'ID1'}>ID1</TextIcon>
        </IconButton>
      ),
      name: 'ID1',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-253.6deg) translate(160px) rotate(253.6deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('ID2', 'Hz', 164)} size="medium">
          <TextIcon active={activeOption === 'ID2'}>ID2</TextIcon>
        </IconButton>
      ),
      name: 'ID2',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-286.32deg) translate(160px) rotate(286.32deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('ID3', 'Hz', 131)} size="medium">
          <TextIcon active={activeOption === 'ID3'}>ID3</TextIcon>
        </IconButton>
      ),
      name: 'ID3',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-319.04deg) translate(160px) rotate(319.04deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('ID4', 'Hz', 98)} size="medium">
          <TextIcon active={activeOption === 'ID4'}>ID4</TextIcon>
        </IconButton>
      ),
      name: 'ID4',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-351.76deg) translate(160px) rotate(351.76deg)',
    },
    {
      icon: (
        <IconButton onClick={onClickButton('RESISTOR', 'Ω', 65)} size="medium">
          <ResistorIcon
            color={
              activeOption === 'RESISTOR'
                ? theme.pallet.secondary.dark
                : theme.pallet.text.hint
            }
            size="1.5em"
          />
        </IconButton>
      ),
      name: 'RESISTOR',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-24.48deg) translate(160px) rotate(24.48deg)',
    },
    {
      icon: (
        <IconButton
          onClick={onClickButton('CAPACITOR', 'pF', 33)}
          size="medium"
        >
          <CapacitorIcon
            color={
              activeOption === 'CAPACITOR'
                ? theme.pallet.secondary.dark
                : theme.pallet.text.hint
            }
            size={'1.5em'}
          />
        </IconButton>
      ),
      name: 'CAPACITOR',
      transform:
        'translateX(-50%) translateY(-50%) rotate(-57.2deg) translate(160px) rotate(57.2deg)',
    },
  ];

  return (
    <InstrumentContainer>
      <Card className={classes.cardMargin}>
        <Dial options={options} value={dialValue} onChangeDial={onChangeDial} />
        <ActionButtons />
      </Card>
      <DisplayContainer>
        <Card>
          <LinearProgress />
          <DisplayWrapper>
            <Display fontSize={'10'} value={data} unit={unit} />
          </DisplayWrapper>
        </Card>
      </DisplayContainer>
    </InstrumentContainer>
  );
};

export default withTheme()(withStyles(styles)(InstrumentCluster));
