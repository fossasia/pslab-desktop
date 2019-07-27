import React from 'react';
import { Switch, Card } from '@material-ui/core';
import {
  InstrumentContainer,
  DisplayContainer,
  SwitchWrapper,
} from './InstrumentCluster.styles';
import Dial from './Dial';
import ActionButtons from './ActionButtons';
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
  onToggleRead,
  dialValue,
  unit,
  isConnected,
  isReading,
  onTogglePulseUnit,
  classes,
  activeCategory,
  isWriting,
  onToggleWrite,
}) => {
  return (
    <InstrumentContainer>
      <MeasurementDisplay unit={unit} isReading={isReading} />
      <DisplayContainer>
        <Card className={classes.cardMargin}>
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
          <ActionButtons
            isReading={isReading}
            isConnected={isConnected}
            onToggleRead={onToggleRead}
            isWriting={isWriting}
            onToggleWrite={onToggleWrite}
          />
        </Card>
      </DisplayContainer>
    </InstrumentContainer>
  );
};

export default withTheme()(withStyles(styles)(InstrumentCluster));
