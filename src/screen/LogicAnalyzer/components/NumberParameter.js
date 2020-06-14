import React, { Component } from 'react';
import {
  Select,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../../utils/formStyles';

class NumberParameters extends Component {
  render() {
    const { numberOfChannels, changeNumberOfChannels, classes } = this.props;

    return (
      <SettingsWrapper>
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              className={classes.label}
              htmlFor="outlined-number-of-channels"
            >
              Number of Channels
            </InputLabel>
            <Select
              value={numberOfChannels}
              onChange={changeNumberOfChannels}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-number-of-channels"
                  id="outlined-number-of-channels"
                />
              }
            >
              {Object.entries(options.NumberOfChannels).map((item, index) => {
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
      </SettingsWrapper>
    );
  }
}

export default withStyles(formStyles)(NumberParameters);
