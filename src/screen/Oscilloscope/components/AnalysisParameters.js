import React, { Component } from 'react';
import ReactDOM from 'react-dom';
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

const styles = () => ({
  formControl: {
    margin: '0px 16px 0px 0px',
  },
});

class AnalysisParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      analysisTypeLabelWidth: 0,
      analysisChannelLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      analysisTypeLabelWidth: ReactDOM.findDOMNode(this.analysisTypeRef)
        .offsetWidth,
      analysisChannelLabelWidth: ReactDOM.findDOMNode(this.analysisChannelRef)
        .offsetWidth,
    });
  }

  render() {
    const {
      isFourierTransformActive,
      transformType,
      transformChannel1,
      transformChannel2,
      onChangeTransformType,
      onChangeTransformChannel,
      onToggleCheckBox,
      classes,
    } = this.props;
    const { analysisTypeLabelWidth, analysisChannelLabelWidth } = this.state;

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
            className={classes.formControl}
            disabled={!isFourierTransformActive}
          >
            <InputLabel
              ref={ref => {
                this.analysisTypeRef = ref;
              }}
              htmlFor="outlined-analysis-type"
            >
              Transform Type
            </InputLabel>
            <Select
              value={transformType}
              onChange={onChangeTransformType}
              input={
                <OutlinedInput
                  labelWidth={analysisTypeLabelWidth}
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
              ref={ref => {
                this.analysisChannelRef = ref;
              }}
              htmlFor="outlined-analysis-channel"
            >
              Channel 1
            </InputLabel>
            <Select
              value={transformChannel1}
              onChange={onChangeTransformChannel('transformChannel1')}
              input={
                <OutlinedInput
                  labelWidth={analysisChannelLabelWidth}
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
            <InputLabel htmlFor="outlined-analysis-channel">
              Channel 2
            </InputLabel>
            <Select
              value={transformChannel2}
              onChange={onChangeTransformChannel('transformChannel2')}
              input={
                <OutlinedInput
                  labelWidth={analysisChannelLabelWidth}
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

export default withStyles(styles)(AnalysisParameters);
