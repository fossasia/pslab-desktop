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

const styles = theme => ({
  cardMargin: {
    margin: '0px 16px 0px 0px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
  },
  switchBase: {
    color: theme.pallet.secondary.dark,
    '&$colorChecked': {
      color: theme.pallet.secondary.dark,
      '& + $colorBar': {
        backgroundColor: theme.pallet.secondary.dark,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

const InstrumentCluster = ({
  activeSubType,
  onClickButton,
  onToggleRead,
  dialValue,
  data,
  unit,
  isConnected,
  isReading,
  classes,
  activeCategory,
  onTogglePulseUnit,
  parameter,
}) => {
  return (
    <InstrumentContainer>
      <Card className={classes.cardMargin}>
        <Dial
          activeSubType={activeSubType}
          value={dialValue}
          onClickButton={onClickButton}
          parameter={parameter}
        />
        {activeCategory === 'PULSE' ? (
          <SwitchWrapper>
            <span>Hz</span>
            <Switch
              color={'default'}
              classes={{
                switchBase: classes.switchBase,
                checked: classes.colorChecked,
                bar: classes.colorBar,
              }}
              onChange={onTogglePulseUnit}
            />
            <span>Count Pulse</span>
          </SwitchWrapper>
        ) : null}
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
