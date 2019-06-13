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
import { withStyles } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import {
  toggleFourierTransform,
  changeFitType,
  changeFitChannel,
} from '../../../redux/actions/oscilloscope';

const styles = () => ({
  formControl: {
    margin: '0px 0px 0px 16px',
  },
});

const AnalysisParameters = ({
  isFourierTransformActive,
  fitType,
  fitChannel1,
  fitChannel2,
  toggleFourierTransform,
  changeFitType,
  changeFitChannel,
  classes,
}) => {
  let ref = {
    analysisType: useRef(),
    analysisChannel: useRef(),
  };

  const [width, setWidth] = useState({
    analysisType: 0,
    analysisChannel: 0,
  });

  useEffect(() => {
    setWidth({
      analysisType: ReactDOM.findDOMNode(ref.analysisType).offsetWidth,
      analysisChannel: ReactDOM.findDOMNode(ref.analysisChannel).offsetWidth,
    });
  });

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
              onChange={toggleFourierTransform}
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
            ref={DOMref => {
              ref.analysisType = DOMref;
            }}
            htmlFor="outlined-analysis-type"
          >
            Fit Type
          </InputLabel>
          <Select
            value={fitType}
            onChange={event => changeFitType({ value: event.target.value })}
            input={
              <OutlinedInput
                labelWidth={width.analysisType}
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
            ref={DOMref => {
              ref.analysisChannel = DOMref;
            }}
            htmlFor="outlined-analysis-channel"
          >
            Channel 1
          </InputLabel>
          <Select
            value={fitChannel1}
            onChange={event =>
              changeFitChannel({
                channelNumber: 'fitChannel1',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.analysisChannel}
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
          <InputLabel htmlFor="outlined-analysis-channel">Channel 2</InputLabel>
          <Select
            value={fitChannel2}
            onChange={event =>
              changeFitChannel({
                channelNumber: 'fitChannel2',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.analysisChannel}
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
};

const mapStateToProps = state => {
  const {
    isFourierTransformActive,
    fitType,
    fitChannel1,
    fitChannel2,
  } = state.oscilloscope;
  return {
    isFourierTransformActive,
    fitType,
    fitChannel1,
    fitChannel2,
  };
};

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      toggleFourierTransform,
      changeFitType,
      changeFitChannel,
    },
    dispatch,
  ),
});

export default withStyles(styles)(
  connect(
    mapStateToProps,
    mapDispatchToProps,
  )(AnalysisParameters),
);
