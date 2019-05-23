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
    margin: '0px 0px 0px 16px',
  },
});

class AnalysisParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      plotChannelLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      plotChannelLabelWidth: ReactDOM.findDOMNode(this.plotChannelRef)
        .offsetWidth,
    });
  }

  render() {
    const {
      isXYPlotActive,
      plotChannel1,
      plotChannel2,
      onToggleCheckBox,
      onChangePlotChannel,
      classes,
    } = this.props;
    const { plotChannelLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          XY Plot
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Checkbox
                checked={isXYPlotActive}
                onChange={onToggleCheckBox('isXYPlotActive')}
              />
            }
            label="Enable XY Plot"
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <FormControl
            variant="outlined"
            fullWidth={true}
            disabled={!isXYPlotActive}
          >
            <InputLabel
              ref={ref => {
                this.plotChannelRef = ref;
              }}
              htmlFor="outlined-trigger-channel"
            >
              Channel 1
            </InputLabel>
            <Select
              value={plotChannel1}
              onChange={onChangePlotChannel('plotChannel1')}
              input={
                <OutlinedInput
                  labelWidth={plotChannelLabelWidth}
                  name="analysis-channel"
                  id="outlined-analysis-channel"
                />
              }
            >
              {Object.entries(options.Select).map((item, index) => {
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
            disabled={!isXYPlotActive}
          >
            <InputLabel htmlFor="outlined-trigger-channel">
              Channel 2
            </InputLabel>
            <Select
              value={plotChannel2}
              onChange={onChangePlotChannel('plotChannel2')}
              input={
                <OutlinedInput
                  labelWidth={plotChannelLabelWidth}
                  name="analysis-channel"
                  id="outlined-analysis-channel"
                />
              }
            >
              {Object.entries(options.Select).map((item, index) => {
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
