import React, { useState, useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import {
  Checkbox,
  Select,
  Typography,
  Divider,
  FormControlLabel,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import CustomSliderInput from '../../../components/CustomSliderInput';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options, timeBaseList } from './settingOptions';
import roundOff from '../../../utils/arithmetics';
import {
  toggleTrigger,
  changeTriggerVoltage,
  changeTriggerChannel,
  ChangeTimeBaseIndex,
} from '../../../redux/actions/oscilloscope';

const TimeParameters = ({
  isTriggerActive,
  triggerVoltage,
  timeBaseIndex,
  timeBase,
  triggerChannel,
  toggleTrigger,
  changeTriggerVoltage,
  changeTriggerChannel,
  ChangeTimeBaseIndex,
}) => {
  let ref = {
    trigger: useRef(),
  };

  const [width, setWidth] = useState({
    trigger: 0,
  });

  useEffect(() => {
    setWidth({
      trigger: ReactDOM.findDOMNode(ref.trigger).offsetWidth,
    });
  }, []);

  return (
    <SettingsWrapper>
      <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
        Timebase and Trigger
      </Typography>
      <Divider />
      <OptionsRowWrapper>
        <FormControlLabel
          control={
            <Checkbox checked={isTriggerActive} onChange={toggleTrigger} />
          }
          label="Trigger"
        />
        <FormControl
          variant="outlined"
          fullWidth={true}
          disabled={!isTriggerActive}
        >
          <InputLabel
            ref={DOMref => {
              ref.trigger = DOMref;
            }}
            htmlFor="outlined-trigger-channel"
          >
            Channel
          </InputLabel>
          <Select
            value={triggerChannel}
            onChange={event =>
              changeTriggerChannel({ value: event.target.value })
            }
            input={
              <OutlinedInput
                labelWidth={width.trigger}
                name="trigger-channel"
                id="outlined-trigger-channel"
              />
            }
          >
            {Object.entries(options.Select).map((item, index) => {
              const key = item[0];
              const value = item[1];
              return (
                <MenuItem key={index} value={key}>
                  {value}
                </MenuItem>
              );
            })}
          </Select>
        </FormControl>
      </OptionsRowWrapper>
      <OptionsRowWrapper>
        <CustomSliderInput
          title="Voltage"
          unit="V"
          onChangeSlider={(event, value) =>
            changeTriggerVoltage({ value: roundOff(value) })
          }
          value={triggerVoltage}
          min={-16.5}
          max={16.5}
          step={0.1}
          disabled={!isTriggerActive}
          minTitleWidth="60px"
          minUnitWidth="66px"
        />
      </OptionsRowWrapper>
      <OptionsRowWrapper>
        <CustomSliderInput
          title="TimeBase"
          unit="ms / div"
          onChangeSlider={(event, value) =>
            ChangeTimeBaseIndex({
              index: value,
              value: timeBaseList[value],
            })
          }
          value={timeBaseIndex}
          min={0}
          max={timeBaseList.length - 1}
          step={1}
          minTitleWidth="60px"
          minUnitWidth="66px"
          display={timeBase}
        />
      </OptionsRowWrapper>
    </SettingsWrapper>
  );
};

const mapStateToProps = state => {
  const {
    isTriggerActive,
    triggerVoltage,
    triggerChannel,
    timeBaseIndex,
    timeBase,
  } = state.oscilloscope;
  return {
    isTriggerActive,
    triggerVoltage,
    triggerChannel,
    timeBaseIndex,
    timeBase,
  };
};

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      toggleTrigger,
      changeTriggerVoltage,
      changeTriggerChannel,
      ChangeTimeBaseIndex,
    },
    dispatch,
  ),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(TimeParameters);
