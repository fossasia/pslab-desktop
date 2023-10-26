import React, { Component } from 'react';
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
import { withStyles } from '@material-ui/core/styles';
import CustomSliderInput from '../../../components/CustomSliderInput';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../../utils/formStyles';

class TimeParameters extends Component {
  render() {
    const {
      triggerVoltage,
      timeBaseListLength,
      timeBaseIndex,
      timeBase,
      triggerChannel,
      isTriggerActive,
      onToggleCheckBox,
      onChangeTriggerVoltage,
      onChangeTriggerChannel,
      onChangeTimeBaseIndex,
      classes,
    } = this.props;
    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Timebase and Trigger
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Checkbox
                checked={isTriggerActive}
                onChange={onToggleCheckBox('isTriggerActive')}
              />
            }
            label="Trigger"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            disabled={!isTriggerActive}
          >
            <InputLabel
              className={classes.label}
              htmlFor="outlined-trigger-channel"
            >
              Channel
            </InputLabel>
            <Select
              value={triggerChannel}
              onChange={onChangeTriggerChannel}
              input={
                <OutlinedInput
                  labelWidth={0}
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
            onChangeSlider={onChangeTriggerVoltage}
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
            onChangeSlider={onChangeTimeBaseIndex}
            value={timeBaseIndex}
            min={0}
            max={timeBaseListLength - 1}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="66px"
            display={timeBase}
          />
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}

export default withStyles(formStyles)(TimeParameters);
