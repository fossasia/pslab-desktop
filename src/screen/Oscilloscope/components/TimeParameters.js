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
import Slider from '@material-ui/lab/Slider';
import { withStyles } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';

const styles = () => ({
  formControl: {
    margin: '0px 16px 0px 0px',
  },
  slider: {
    margin: '0px 16px 0px 0px',
  },
});

class TimeParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      triggerLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      triggerLabelWidth: ReactDOM.findDOMNode(this.triggerRef).offsetWidth,
    });
  }

  render() {
    const {
      onToggleCheckBox,
      onChangeTriggerVoltage,
      onChangeTriggerChannel,
      onChangeTimeBase,
      triggerVoltage,
      timeBase,
      triggerVoltageChannel,
      isTriggerActive,
      classes,
    } = this.props;
    const { triggerLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Timebase and Trigger
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Checkbox
                checked={isTriggerActive}
                onChange={onToggleCheckBox('isTriggerActive')}
              />
            }
            label="Trigger"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
            disabled={!isTriggerActive}
          >
            <InputLabel
              ref={ref => {
                this.triggerRef = ref;
              }}
              htmlFor="outlined-trigger-channel"
            >
              Channel
            </InputLabel>
            <Select
              value={triggerVoltageChannel}
              onChange={onChangeTriggerChannel}
              input={
                <OutlinedInput
                  labelWidth={triggerLabelWidth}
                  name="trigger-channel"
                  id="outlined-trigger-channel"
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
          <Slider
            classes={{ container: classes.slider }}
            disabled={!isTriggerActive}
            step={0.5}
            value={triggerVoltage}
            min={-16.5}
            max={16.5}
            onChange={onChangeTriggerVoltage}
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <span style={{ marginRight: 16 }}>TimeBase</span>
          <Slider
            classes={{ container: classes.slider }}
            step={1}
            value={timeBase}
            min={10}
            max={800}
            onChange={onChangeTimeBase}
          />
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}

export default withStyles(styles)(TimeParameters);
