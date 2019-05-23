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
  sqr1colorSwitchBase: {
    color: theme.pallet.sqr1Color,
    '&$colorChecked': {
      color: theme.pallet.sqr1Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.sqr1Color,
      },
    },
  },
  sqr2colorSwitchBase: {
    color: theme.pallet.sqr2Color,
    '&$colorChecked': {
      color: theme.pallet.sqr2Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.sqr2Color,
      },
    },
  },
  sqr3colorSwitchBase: {
    color: theme.pallet.sqr3Color,
    '&$colorChecked': {
      color: theme.pallet.sqr3Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.sqr3Color,
      },
    },
  },
  sqr4colorSwitchBase: {
    color: theme.pallet.sqr4Color,
    '&$colorChecked': {
      color: theme.pallet.sqr4Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.sqr4Color,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class SquareWaveParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ModeLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      ModeLabelWidth: ReactDOM.findDOMNode(this.ModeRef).offsetWidth,
    });
  }

  render() {
    const {
      activePreview,
      mode,
      sqr1Frequency,
      sqr1DutyCycle,
      sqr2Frequency,
      sqr2DutyCycle,
      sqr2Phase,
      sqr3Frequency,
      sqr3DutyCycle,
      sqr3Phase,
      sqr4Frequency,
      sqr4DutyCycle,
      sqr4Phase,
      onTogglePreview,
      onChangeMode,
      onChangeSlider,
      classes,
    } = this.props;
    const { ModeLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Digital
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              ref={ref => {
                this.ModeRef = ref;
              }}
              htmlFor="outlined-mode"
            >
              Mode
            </InputLabel>
            <Select
              value={mode}
              onChange={onChangeMode}
              input={
                <OutlinedInput
                  labelWidth={ModeLabelWidth}
                  name="outlined-mode"
                  id="outlined-mode"
                />
              }
            >
              {Object.entries(options.Mode).map((item, index) => {
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
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activePreview.sqr1}
                onChange={onTogglePreview('sqr1')}
                value={'SQR1'}
                classes={{
                  switchBase: classes.sqr1colorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="SQR1"
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <CustomSliderInput
            title="Frequency"
            unit="Hz"
            onChangeSlider={onChangeSlider('sqr1Frequency')}
            value={sqr1Frequency}
            min={10}
            max={5000}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="40px"
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <CustomSliderInput
            title="Duty Cycle"
            unit="%"
            onChangeSlider={onChangeSlider('sqr1DutyCycle')}
            value={sqr1DutyCycle}
            min={0}
            max={100}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="40px"
          />
        </OptionsRowWrapper>
        {mode === 'pwm' && <Divider />}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <FormControlLabel
              control={
                <Switch
                  checked={activePreview.sqr2}
                  onChange={onTogglePreview('sqr2')}
                  value={'SQR2'}
                  classes={{
                    switchBase: classes.sqr2colorSwitchBase,
                    checked: classes.colorChecked,
                    bar: classes.colorBar,
                  }}
                />
              }
              label="SQR2"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Frequency"
              unit="Hz"
              onChangeSlider={onChangeSlider('sqr2Frequency')}
              value={sqr2Frequency}
              min={10}
              max={5000}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Duty Cycle"
              unit="%"
              onChangeSlider={onChangeSlider('sqr2DutyCycle')}
              value={sqr2DutyCycle}
              min={0}
              max={100}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Phase"
              unit="Deg"
              onChangeSlider={onChangeSlider('sqr2Phase')}
              value={sqr2Phase}
              min={0}
              max={360}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && <Divider />}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <FormControlLabel
              control={
                <Switch
                  checked={activePreview.sqr3}
                  onChange={onTogglePreview('sqr3')}
                  value={'SQR3'}
                  classes={{
                    switchBase: classes.sqr3colorSwitchBase,
                    checked: classes.colorChecked,
                    bar: classes.colorBar,
                  }}
                />
              }
              label="SQR3"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Frequency"
              unit="Hz"
              onChangeSlider={onChangeSlider('sqr3Frequency')}
              value={sqr3Frequency}
              min={10}
              max={5000}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Duty Cycle"
              unit="%"
              onChangeSlider={onChangeSlider('sqr3DutyCycle')}
              value={sqr3DutyCycle}
              min={0}
              max={100}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Phase"
              unit="Deg"
              onChangeSlider={onChangeSlider('sqr3Phase')}
              value={sqr3Phase}
              min={0}
              max={360}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && <Divider />}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <FormControlLabel
              control={
                <Switch
                  checked={activePreview.sqr4}
                  onChange={onTogglePreview('sqr4')}
                  value={'SQR4'}
                  classes={{
                    switchBase: classes.sqr4colorSwitchBase,
                    checked: classes.colorChecked,
                    bar: classes.colorBar,
                  }}
                />
              }
              label="SQR4"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Frequency"
              unit="Hz"
              onChangeSlider={onChangeSlider('sqr4Frequency')}
              value={sqr4Frequency}
              min={10}
              max={5000}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Duty Cycle"
              unit="%"
              onChangeSlider={onChangeSlider('sqr4DutyCycle')}
              value={sqr4DutyCycle}
              min={0}
              max={100}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
        {mode === 'pwm' && (
          <OptionsRowWrapper>
            <CustomSliderInput
              title="Phase"
              unit="Deg"
              onChangeSlider={onChangeSlider('sqr4Phase')}
              value={sqr4Phase}
              min={0}
              max={360}
              step={1}
              minTitleWidth="60px"
              minUnitWidth="40px"
            />
          </OptionsRowWrapper>
        )}
      </SettingsWrapper>
    );
  }
}

export default withTheme()(withStyles(styles)(SquareWaveParameters));
