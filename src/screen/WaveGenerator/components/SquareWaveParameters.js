import React from 'react';
import {
  Typography,
  Divider,
  FormControlLabel,
  Switch,
} from '@material-ui/core';
import CustomSliderInput from '../../../components/CustomSliderInput';
import { withStyles, withTheme } from '@material-ui/core/styles';
import {
  SettingsWrapper,
  OptionsRowWrapper,
  TitleWrapper,
  Spacer,
} from './Settings.styles';

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

const SquareWaveParameters = ({
  digital,
  pwmFrequency,
  sqr1DutyCycle,
  sqr2DutyCycle,
  sqr2Phase,
  sqr3DutyCycle,
  sqr3Phase,
  sqr4DutyCycle,
  sqr4Phase,
  onTogglePreview,
  onChangeSlider,
  classes,
}) => (
  <SettingsWrapper>
    <TitleWrapper>
      <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
        Digital
      </Typography>
      <Spacer />
      <FormControlLabel
        control={
          <Switch
            checked={digital}
            onChange={onTogglePreview}
            value={'digital'}
            classes={{
              switchBase: classes.sqr1colorSwitchBase,
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
        SQ1 pin
      </Typography>
    </OptionsRowWrapper>
    <OptionsRowWrapper>
      <CustomSliderInput
        title="Frequency"
        unit="Hz"
        onChangeSlider={onChangeSlider('pwmFrequency')}
        value={pwmFrequency}
        min={10}
        max={5000}
        step={1}
        minTitleWidth="60px"
        minUnitWidth="40px"
        disabled={!digital}
      />
    </OptionsRowWrapper>
    <Divider />
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
    <Divider />
    <OptionsRowWrapper>
      <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
        SQ2 pin
      </Typography>
    </OptionsRowWrapper>
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
    <Divider />
    <OptionsRowWrapper>
      <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
        SQ3 pin
      </Typography>
    </OptionsRowWrapper>
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
    <Divider />
    <OptionsRowWrapper>
      <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
        SQ4 pin
      </Typography>
    </OptionsRowWrapper>
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
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
        disabled={!digital}
      />
    </OptionsRowWrapper>
  </SettingsWrapper>
);

export default withTheme()(withStyles(styles)(SquareWaveParameters));
