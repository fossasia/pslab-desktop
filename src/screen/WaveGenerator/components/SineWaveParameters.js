import React, { Component } from 'react';
import ReactDOM from 'react-dom';
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
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';

const styles = theme => ({
  s1colorSwitchBase: {
    color: theme.pallet.s1Color,
    '&$colorChecked': {
      color: theme.pallet.s1Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.s1Color,
      },
    },
  },
  s2colorSwitchBase: {
    color: theme.pallet.s2Color,
    '&$colorChecked': {
      color: theme.pallet.s2Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.s2Color,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class SineWaveParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      WaveFormLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      WaveFormLabelWidth: ReactDOM.findDOMNode(this.WaveFormRef).offsetWidth,
    });
  }

  render() {
    const {
      activePreview,
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
    const { WaveFormLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Wave Form
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activePreview.s1}
                onChange={onTogglePreview('s1')}
                value={'S1'}
                classes={{
                  switchBase: classes.s1colorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="S1"
          />
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              ref={ref => {
                this.WaveFormRef = ref;
              }}
              htmlFor="outlined-waveform-s1"
            >
              Wave Type
            </InputLabel>
            <Select
              value={waveFormS1}
              onChange={onChangeWaveForm('waveFormS1')}
              input={
                <OutlinedInput
                  labelWidth={WaveFormLabelWidth}
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
          />
        </OptionsRowWrapper>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activePreview.s2}
                onChange={onTogglePreview('s2')}
                value={'S2'}
                classes={{
                  switchBase: classes.s2colorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="S2"
          />
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel htmlFor="outlined-waveform-s2">Wave Type</InputLabel>
            <Select
              value={waveFormS2}
              onChange={onChangeWaveForm('waveFormS2')}
              input={
                <OutlinedInput
                  labelWidth={WaveFormLabelWidth}
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
          />
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}

export default withTheme()(withStyles(styles)(SineWaveParameters));
