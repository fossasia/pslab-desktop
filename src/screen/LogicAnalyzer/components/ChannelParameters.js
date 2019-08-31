import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {
  Select,
  Typography,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';

const styles = theme => ({
  formControl: {
    margin: '0px 0px 0px 16px',
  },
});

class ChannelParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      MapLabelWidth: 0,
      TriggerLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      MapLabelWidth: ReactDOM.findDOMNode(this.MapRef).offsetWidth,
      TriggerLabelWidth: ReactDOM.findDOMNode(this.TriggerRef).offsetWidth,
    });
  }

  render() {
    const {
      numberOfChannels,
      channel1Map,
      channel2Map,
      trigger1Type,
      trigger2Type,
      trigger3Type,
      trigger4Type,
      changeChannelMap,
      changeTriggerType,
      classes,
    } = this.props;
    const { MapLabelWidth, TriggerLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Channel Parameters
        </Typography>
        <OptionsRowWrapper>
          <Typography component="h6" variant="subheading">
            LA1
          </Typography>
          {numberOfChannels <= 2 && (
            <FormControl
              className={classes.formControl}
              variant="outlined"
              fullWidth={true}
            >
              <InputLabel
                ref={ref => {
                  this.MapRef = ref;
                }}
                htmlFor="outlined-map-la1"
              >
                Mapped to
              </InputLabel>
              <Select
                value={channel1Map}
                onChange={changeChannelMap('channel1Map')}
                input={
                  <OutlinedInput
                    labelWidth={MapLabelWidth}
                    name="outlined-map-la1"
                    id="outlined-map-la1"
                  />
                }
              >
                {Object.entries(options.ChannelMap).map((item, index) => {
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
          )}
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel
              ref={ref => {
                this.TriggerRef = ref;
              }}
              htmlFor="outlined-trigger-la1"
            >
              Trigger Type
            </InputLabel>
            <Select
              value={trigger1Type}
              onChange={changeTriggerType('trigger1Type')}
              input={
                <OutlinedInput
                  labelWidth={TriggerLabelWidth}
                  name="outlined-trigger-la1"
                  id="outlined-trigger-la1"
                />
              }
            >
              {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        {numberOfChannels > 1 && (
          <OptionsRowWrapper>
            <Typography component="h6" variant="subheading">
              LA2
            </Typography>
            {numberOfChannels <= 2 && (
              <FormControl
                className={classes.formControl}
                variant="outlined"
                fullWidth={true}
              >
                <InputLabel htmlFor="outlined-map-la2">Mapped to</InputLabel>
                <Select
                  value={channel2Map}
                  onChange={changeChannelMap('channel2Map')}
                  input={
                    <OutlinedInput
                      labelWidth={MapLabelWidth}
                      name="outlined-map-la2"
                      id="outlined-map-la2"
                    />
                  }
                >
                  {Object.entries(options.ChannelMap).map((item, index) => {
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
            )}
            <FormControl
              variant="outlined"
              fullWidth={true}
              className={classes.formControl}
            >
              <InputLabel htmlFor="outlined-trigger-la2">
                Trigger Type
              </InputLabel>
              <Select
                value={trigger2Type}
                onChange={changeTriggerType('trigger2Type')}
                input={
                  <OutlinedInput
                    labelWidth={TriggerLabelWidth}
                    name="outlined-trigger-la2"
                    id="outlined-trigger-la2"
                  />
                }
              >
                {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        )}
        {numberOfChannels > 2 && (
          <OptionsRowWrapper>
            <Typography component="h6" variant="subheading">
              LA3
            </Typography>
            <FormControl
              variant="outlined"
              fullWidth={true}
              className={classes.formControl}
            >
              <InputLabel htmlFor="outlined-trigger-la3">
                Trigger Type
              </InputLabel>
              <Select
                value={trigger3Type}
                onChange={changeTriggerType('trigger3Type')}
                input={
                  <OutlinedInput
                    labelWidth={TriggerLabelWidth}
                    name="outlined-trigger-la3"
                    id="outlined-trigger-la3"
                  />
                }
              >
                {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        )}
        {numberOfChannels > 3 && (
          <OptionsRowWrapper>
            <Typography component="h6" variant="subheading">
              LA4
            </Typography>
            <FormControl
              variant="outlined"
              fullWidth={true}
              className={classes.formControl}
            >
              <InputLabel htmlFor="outlined-trigger-la4">
                Trigger Type
              </InputLabel>
              <Select
                value={trigger4Type}
                onChange={changeTriggerType('trigger4Type')}
                input={
                  <OutlinedInput
                    labelWidth={TriggerLabelWidth}
                    name="outlined-trigger-la4"
                    id="outlined-trigger-la4"
                  />
                }
              >
                {Object.entries(options.ChannelTrigger).map((item, index) => {
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
        )}
      </SettingsWrapper>
    );
  }
}

export default withStyles(styles)(ChannelParameters);
