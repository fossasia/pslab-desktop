import React from 'react';
import { Card, Button, Typography, Divider } from '@material-ui/core';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import {
  InstrumentContainer,
  SwitchContainer,
  SwitchWrapper,
  DisplayContainer,
  DisplayWrapper,
} from './InstrumentCluster.styles';
import Display from '../../../components/Display';

const InstrumentCluster = props => (
  <InstrumentContainer>
    <SwitchContainer>
      <Card>
        <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
          Measure
        </Typography>
        <Divider />
        <SwitchWrapper>
          <FormControl
            component="fieldset"
            // className={classes.formControl}
          >
            <RadioGroup
              aria-label="Gender"
              name="gender1"
              // className={classes.group}
              value={'x'}
              onChange={() => {}}
            >
              <FormControlLabel
                value="male"
                control={<Radio />}
                label="Resistance"
              />
              <FormControlLabel
                value="male"
                control={<Radio />}
                label="Capacitence"
              />
            </RadioGroup>
          </FormControl>
        </SwitchWrapper>
      </Card>
      <Card>
        <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
          Voltage
        </Typography>
        <Divider />
        <SwitchWrapper>
          <FormControl
            component="fieldset"
            // className={classes.formControl}
          >
            <RadioGroup
              aria-label="Gender"
              name="gender1"
              // className={classes.group}
              value={'x'}
              onChange={() => {}}
            >
              <FormControlLabel value="male" control={<Radio />} label="ID1" />
              <FormControlLabel value="male" control={<Radio />} label="ID2" />
              <FormControlLabel value="male" control={<Radio />} label="ID3" />
              <FormControlLabel value="male" control={<Radio />} label="ID4" />
            </RadioGroup>
          </FormControl>
        </SwitchWrapper>
      </Card>
    </SwitchContainer>
    <DisplayContainer>
      <Card>
        <DisplayWrapper>
          {' '}
          <Display value={20} unit={'V'} />
        </DisplayWrapper>
      </Card>
    </DisplayContainer>
    <SwitchContainer>
      <Card>
        <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
          Voltage
        </Typography>
        <Divider />
        <SwitchWrapper>
          <FormControl
            component="fieldset"
            // className={classes.formControl}
          >
            <RadioGroup
              aria-label="Gender"
              name="gender1"
              // className={classes.group}
              value={'x'}
              onChange={() => {}}
            >
              <FormControlLabel value="male" control={<Radio />} label="CH1" />
              <FormControlLabel value="male" control={<Radio />} label="CH2" />
              <FormControlLabel value="male" control={<Radio />} label="CH3" />
              <FormControlLabel value="male" control={<Radio />} label="CAP" />
              <FormControlLabel value="male" control={<Radio />} label="AN8" />
            </RadioGroup>
          </FormControl>
        </SwitchWrapper>
      </Card>
    </SwitchContainer>
  </InstrumentContainer>
);

export default InstrumentCluster;
