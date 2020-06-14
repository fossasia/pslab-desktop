import React, { Component } from 'react';
import {
  Select,
  Typography,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../../utils/formStyles';

class ChannelParameters extends Component {
  render() {
    const {
      numberOfChannels,
      channel1Map,
      channel2Map,
      trigger1Type,
      trigger2Type,
      trigger3Type,
      trigger4Type,
      changeChannelMap,
      changeTriggerType,
      classes,
    } = this.props;
    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Channel Parameters
        </Typography>
        <OptionsRowWrapper>
          <Typography component="h6" variant="subtitle1">
            LA1
          </Typography>
          {numberOfChannels <= 2 && (
            <FormControl
              className={classes.formControl}
              variant="outlined"
              fullWidth={true}
            >
              <InputLabel className={classes.label} htmlFor="outlined-map-la1">
                Mapped to
              </InputLabel>
              <Select
                value={channel1Map}
                onChange={changeChannelMap('channel1Map')}
                input={
                  <OutlinedInput
                    labelWidth={0}
                    name="outlined-map-la1"
                    id="outlined-map-la1"
                  />
                }
              >
                {Object.entries(options.ChannelMap).map((item, index) => {
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
          )}
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel
              className={classes.label}
              htmlFor="outlined-trigger-la1"
            >
              Trigger Type
            </InputLabel>
            <Select
              value={trigger1Type}
              onChange={changeTriggerType('trigger1Type')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-trigger-la1"
                  id="outlined-trigger-la1"
                />
              }
            >
              {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        {numberOfChannels > 1 && (
          <OptionsRowWrapper>
            <Typography component="h6" variant="subtitle1">
              LA2
            </Typography>
            {numberOfChannels <= 2 && (
              <FormControl
                className={classes.formControl}
                variant="outlined"
                fullWidth={true}
              >
                <InputLabel
                  className={classes.label}
                  htmlFor="outlined-map-la2"
                >
                  Mapped to
                </InputLabel>
                <Select
                  value={channel2Map}
                  onChange={changeChannelMap('channel2Map')}
                  input={
                    <OutlinedInput
                      labelWidth={0}
                      name="outlined-map-la2"
                      id="outlined-map-la2"
                    />
                  }
                >
                  {Object.entries(options.ChannelMap).map((item, index) => {
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
            )}
            <FormControl
              variant="outlined"
              fullWidth={true}
              className={classes.formControl}
            >
              <InputLabel
                className={classes.label}
                htmlFor="outlined-trigger-la2"
              >
                Trigger Type
              </InputLabel>
              <Select
                value={trigger2Type}
                onChange={changeTriggerType('trigger2Type')}
                input={
                  <OutlinedInput
                    labelWidth={0}
                    name="outlined-trigger-la2"
                    id="outlined-trigger-la2"
                  />
                }
              >
                {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        )}
        {numberOfChannels > 2 && (
          <OptionsRowWrapper>
            <Typography component="h6" variant="subtitle1">
              LA3
            </Typography>
            <FormControl
              variant="outlined"
              fullWidth={true}
              className={classes.formControl}
            >
              <InputLabel
                className={classes.label}
                htmlFor="outlined-trigger-la3"
              >
                Trigger Type
              </InputLabel>
              <Select
                value={trigger3Type}
                onChange={changeTriggerType('trigger3Type')}
                input={
                  <OutlinedInput
                    labelWidth={0}
                    name="outlined-trigger-la3"
                    id="outlined-trigger-la3"
                  />
                }
              >
                {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        )}
        {numberOfChannels > 3 && (
          <OptionsRowWrapper>
            <Typography component="h6" variant="subtitle1">
              LA4
            </Typography>
            <FormControl
              variant="outlined"
              fullWidth={true}
              className={classes.formControl}
            >
              <InputLabel
                className={classes.label}
                htmlFor="outlined-trigger-la4"
              >
                Trigger Type
              </InputLabel>
              <Select
                value={trigger4Type}
                onChange={changeTriggerType('trigger4Type')}
                input={
                  <OutlinedInput
                    labelWidth={0}
                    name="outlined-trigger-la4"
                    id="outlined-trigger-la4"
                  />
                }
              >
                {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        )}
      </SettingsWrapper>
    );
  }
}

export default withStyles(formStyles)(ChannelParameters);
