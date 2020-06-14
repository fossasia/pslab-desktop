import React, { Component } from 'react';
import {
  Select,
  Typography,
  Divider,
  FormControlLabel,
  MenuItem,
  Switch,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import { withStyles, withTheme } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../../utils/formStyles';

const styles = theme => ({
  ch1ColorSwitchBase: {
    color: theme.palette.ch1Color,
    '&$colorChecked': {
      color: theme.palette.ch1Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.ch1Color,
      },
    },
  },
  ch2ColorSwitchBase: {
    color: theme.palette.ch2Color,
    '&$colorChecked': {
      color: theme.palette.ch2Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.ch2Color,
      },
    },
  },
  ch3ColorSwitchBase: {
    color: theme.palette.ch3Color,
    '&$colorChecked': {
      color: theme.palette.ch3Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.ch3Color,
      },
    },
  },
  micColorSwitchBase: {
    color: theme.palette.micColor,
    '&$colorChecked': {
      color: theme.palette.micColor,
      '& + $colorBar': {
        backgroundColor: theme.palette.micColor,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class ChannelParameters extends Component {
  render() {
    const {
      activeChannels,
      channelRanges,
      channelMaps,
      onToggleChannel,
      onChangeChannelRange,
      onChangeChannelMap,
      classes,
    } = this.props;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Channel Parameters
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.ch1}
                onChange={onToggleChannel('ch1')}
                value={'CH1'}
                classes={{
                  switchBase: classes.ch1ColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH1"
          />
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel className={classes.label} htmlFor="outlined-range-ch1">
              Range
            </InputLabel>
            <Select
              value={channelRanges.ch1}
              onChange={onChangeChannelRange('ch1')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-range-ch1"
                  id="outlined-range-ch1"
                />
              }
            >
              {Object.entries(options.Range1).map((item, index) => {
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
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel className={classes.label} htmlFor="outlined-map-ch1">
              Mapped To
            </InputLabel>
            <Select
              value={channelMaps.ch1}
              onChange={onChangeChannelMap('ch1')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-map-ch1"
                  id="outlined-map-ch1"
                />
              }
            >
              {Object.entries(options.Map1).map((item, index) => {
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
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.ch2}
                onChange={onToggleChannel('ch2')}
                value={'ch2'}
                classes={{
                  switchBase: classes.ch2ColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH2"
          />
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel className={classes.label} htmlFor="outlined-range-ch2">
              Range
            </InputLabel>
            <Select
              value={channelRanges.ch2}
              onChange={onChangeChannelRange('ch2')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-range-ch2"
                  id="outlined-range-ch2"
                />
              }
            >
              {Object.entries(options.Range1).map((item, index) => {
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
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel className={classes.label} htmlFor="outlined-map-ch2">
              Mapped To
            </InputLabel>
            <Select
              value={channelMaps.ch2}
              onChange={onChangeChannelMap('ch2')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-map-ch2"
                  id="outlined-map-ch2"
                />
              }
            >
              {Object.entries(options.Map1).map((item, index) => {
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
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.ch3}
                onChange={onToggleChannel('ch3')}
                value={'ch3'}
                classes={{
                  switchBase: classes.ch3ColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH3"
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.mic}
                onChange={onToggleChannel('mic')}
                value={'mic'}
                classes={{
                  switchBase: classes.micColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="MIC"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            disabled={!activeChannels.mic}
          >
            <InputLabel className={classes.label} htmlFor="outlined-map-mic">
              Mic Type
            </InputLabel>
            <Select
              value={channelMaps.mic}
              onChange={onChangeChannelMap('mic')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-map-mic"
                  id="outlined-map-mic"
                />
              }
            >
              {Object.entries(options.Mic).map((item, index) => {
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

export default withTheme(
  withStyles({ ...styles, ...formStyles })(ChannelParameters),
);
