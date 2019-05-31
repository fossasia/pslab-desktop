import React from 'react';
import { Switch, Card } from '@material-ui/core';
import {
  InstrumentContainer,
  DisplayContainer,
  DisplayWrapper,
  SwitchWrapper,
} from './InstrumentCluster.styles';
import LinearProgress from '@material-ui/core/LinearProgress';
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
  activeSubType,
  onClickButton,
  changeOption,
  onToggleRead,
  dialValue,
  data,
  unit,
  isConnected,
  isReading,
  onTogglePulseUnit,
  classes,
  activeCategory,
}) => {
  return (
    <InstrumentContainer>
      <Card className={classes.cardMargin}>
        <Dial
          activeSubType={activeSubType}
          value={dialValue}
          onClickButton={onClickButton}
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
        />
      </Card>
      <DisplayContainer>
        <Card>
          {isReading && <LinearProgress />}
          <DisplayWrapper>
            <Display fontSize={'10'} value={data} unit={unit} />
          </DisplayWrapper>
        </Card>
      </DisplayContainer>
    </InstrumentContainer>
  );
};

export default withTheme()(withStyles(styles)(InstrumentCluster));
