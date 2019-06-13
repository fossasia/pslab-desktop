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
  toggleXYPlot,
  changePlotChannel,
} from '../../../redux/actions/oscilloscope';

const styles = () => ({
  formControl: {
    margin: '0px 0px 0px 16px',
  },
});

const AnalysisParameters = ({
  isXYPlotActive,
  plotChannel1,
  plotChannel2,
  toggleXYPlot,
  changePlotChannel,
  classes,
}) => {
  let ref = {
    plotChannel: useRef(),
  };

  const [width, setWidth] = useState({
    plotChannel: 0,
  });

  useEffect(() => {
    setWidth({
      plotChannel: ReactDOM.findDOMNode(ref.plotChannel).offsetWidth,
    });
  }, []);

  return (
    <SettingsWrapper>
      <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
        XY Plot
      </Typography>
      <Divider />
      <OptionsRowWrapper>
        <FormControlLabel
          control={
            <Checkbox checked={isXYPlotActive} onChange={toggleXYPlot} />
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
            ref={DOMref => {
              ref.plotChannel = DOMref;
            }}
            htmlFor="outlined-trigger-channel"
          >
            Channel 1
          </InputLabel>
          <Select
            value={plotChannel1}
            onChange={event =>
              changePlotChannel({
                channelNumber: 'plotChannel1',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.plotChannel}
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
          <InputLabel htmlFor="outlined-trigger-channel">Channel 2</InputLabel>
          <Select
            value={plotChannel2}
            onChange={event =>
              changePlotChannel({
                channelNumber: 'plotChannel2',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.plotChannel}
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
};

const mapStateToProps = state => {
  const { isXYPlotActive, plotChannel1, plotChannel2 } = state.oscilloscope;
  return {
    isXYPlotActive,
    plotChannel1,
    plotChannel2,
  };
};

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      toggleXYPlot,
      changePlotChannel,
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
