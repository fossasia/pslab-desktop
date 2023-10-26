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
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../../utils/formStyles';

class AnalysisParameters extends Component {
  render() {
    const {
      isFourierTransformActive,
      fitType,
      fitChannel1,
      fitChannel2,
      onChangeFitType,
      onChangeFitChannel,
      onToggleCheckBox,
      classes,
    } = this.props;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Data Analysis
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Checkbox
                checked={isFourierTransformActive}
                onChange={onToggleCheckBox('isFourierTransformActive')}
              />
            }
            label="Fourier Transforms"
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <FormControl
            variant="outlined"
            fullWidth={true}
            disabled={!isFourierTransformActive}
          >
            <InputLabel
              className={classes.label}
              htmlFor="outlined-analysis-type"
            >
              Fit Type
            </InputLabel>
            <Select
              value={fitType}
              onChange={onChangeFitType}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="analysis-type"
                  id="outlined-analysis-type"
                />
              }
            >
              {Object.entries(options.FitSelect).map((item, index) => {
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
            disabled={!isFourierTransformActive}
          >
            <InputLabel
              className={classes.label}
              htmlFor="outlined-analysis-channel"
            >
              Channel 1
            </InputLabel>
            <Select
              value={fitChannel1}
              onChange={onChangeFitChannel('fitChannel1')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="analysis-channel"
                  id="outlined-analysis-channel"
                />
              }
            >
              {Object.entries(options.DataAnalysisSelect).map((item, index) => {
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
            disabled={!isFourierTransformActive}
          >
            <InputLabel
              className={classes.label}
              htmlFor="outlined-analysis-channel"
            >
              Channel 2
            </InputLabel>
            <Select
              value={fitChannel2}
              onChange={onChangeFitChannel('fitChannel2')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="analysis-channel"
                  id="outlined-analysis-channel"
                />
              }
            >
              {Object.entries(options.DataAnalysisSelect).map((item, index) => {
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

export default withStyles(formStyles)(AnalysisParameters);
