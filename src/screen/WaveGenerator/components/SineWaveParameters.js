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
import CustomSliderInput from '../../../components/CustomSliderInput';
import { withStyles, withTheme } from '@material-ui/core/styles';
import {
  SettingsWrapper,
  OptionsRowWrapper,
  TitleWrapper,
  Spacer,
} from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../../utils/formStyles';

const styles = theme => ({
  s1colorSwitchBase: {
    color: theme.palette.s1Color,
    '&$colorChecked': {
      color: theme.palette.s1Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.s1Color,
      },
    },
  },
  s2colorSwitchBase: {
    color: theme.palette.s2Color,
    '&$colorChecked': {
      color: theme.palette.s2Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.s2Color,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class SineWaveParameters extends Component {
  render() {
    const {
      wave,
      s1Frequency,
      s2Frequency,
      s2Phase,
      waveFormS1,
      waveFormS2,
      onTogglePreview,
      onChangeWaveForm,
      onChangeSlider,
      classes,
    } = this.props;
    return (
      <SettingsWrapper>
        <TitleWrapper>
          <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
            Wave Form
          </Typography>
          <Spacer />
          <FormControlLabel
            control={
              <Switch
                checked={wave}
                onChange={onTogglePreview}
                value={'wave'}
                classes={{
                  switchBase: classes.s1colorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
          />
        </TitleWrapper>
        <Divider />
        <OptionsRowWrapper>
          <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
            S1 pin
          </Typography>
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              className={classes.label}
              htmlFor="outlined-waveform-s1"
            >
              Wave Type
            </InputLabel>
            <Select
              value={waveFormS1}
              onChange={onChangeWaveForm('waveFormS1')}
              disabled={!wave}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-waveform-s1"
                  id="outlined-waveform-s1"
                />
              }
            >
              {Object.entries(options.WaveForm).map((item, index) => {
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
            title="Frequency"
            unit="Hz"
            onChangeSlider={onChangeSlider('s1Frequency')}
            value={s1Frequency}
            min={10}
            max={5000}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="40px"
            disabled={!wave}
          />
        </OptionsRowWrapper>
        <Divider />
        <OptionsRowWrapper>
          <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
            S2 pin
          </Typography>
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              className={classes.label}
              htmlFor="outlined-waveform-s2"
            >
              Wave Type
            </InputLabel>
            <Select
              value={waveFormS2}
              onChange={onChangeWaveForm('waveFormS2')}
              disabled={!wave}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-waveform-s2"
                  id="outlined-waveform-s2"
                />
              }
            >
              {Object.entries(options.WaveForm).map((item, index) => {
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
            title="Frequency"
            unit="Hz"
            onChangeSlider={onChangeSlider('s2Frequency')}
            value={s2Frequency}
            min={10}
            max={5000}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="40px"
            disabled={!wave}
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <CustomSliderInput
            title="Phase"
            unit="Deg"
            onChangeSlider={onChangeSlider('s2Phase')}
            value={s2Phase}
            min={0}
            max={360}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="40px"
            disabled={!wave}
          />
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}

export default withTheme(
  withStyles({ ...styles, ...formStyles })(SineWaveParameters),
);
