import React from 'react';
import { Switch, Card } from '@material-ui/core';
import {
  InstrumentContainer,
  DisplayContainer,
  SwitchWrapper,
  Backdrop,
  TopSection,
  BottomSection,
  ResSection,
  WaveSection,
} from './InstrumentCluster.styles';
import Dial from './Dial';
import { withTheme, withStyles } from '@material-ui/core/styles';
import MeasurementDisplay from './MeasurementDisplay';

const styles = () => ({
  cardMargin: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
  },
});

const InstrumentCluster = ({
  activeSubType,
  onClickButton,
  changeDialValue,
  changeOption,
  dialValue,
  unit,
  isReading,
  onTogglePulseUnit,
  classes,
  activeCategory,
}) => {
  return (
    <InstrumentContainer>
      <MeasurementDisplay unit={unit} isReading={isReading} />
      <DisplayContainer>
        <Card
          className={classes.cardMargin}
          style={{
            height: '590px',
            position: 'relative',
          }}
        >
          <Backdrop>
            <TopSection>Voltage</TopSection>
            <BottomSection>
              <WaveSection></WaveSection>
              <ResSection>Measure</ResSection>
            </BottomSection>
          </Backdrop>
          <Dial
            activeSubType={activeSubType}
            value={dialValue}
            onClickButton={onClickButton}
            changeDialValue={changeDialValue}
            changeOption={changeOption}
          />
          <SwitchWrapper>
            <span>Hz</span>
            <Switch
              disabled={activeCategory !== 'PULSE'}
              onChange={onTogglePulseUnit}
              color="secondary"
            />
            <span>Count Pulse</span>
          </SwitchWrapper>
        </Card>
      </DisplayContainer>
    </InstrumentContainer>
  );
};

export default withTheme(withStyles(styles)(InstrumentCluster));
