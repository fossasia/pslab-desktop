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
import { withStyles, withTheme } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';

const styles = theme => ({
  formControl: {
    margin: '0px 0px 0px 16px',
  },
  ch1ColorSwitchBase: {
    color: theme.pallet.ch1Color,
    '&$colorChecked': {
      color: theme.pallet.ch1Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.ch1Color,
      },
    },
  },
  ch2ColorSwitchBase: {
    color: theme.pallet.ch2Color,
    '&$colorChecked': {
      color: theme.pallet.ch2Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.ch2Color,
      },
    },
  },
  ch3ColorSwitchBase: {
    color: theme.pallet.ch3Color,
    '&$colorChecked': {
      color: theme.pallet.ch3Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.ch3Color,
      },
    },
  },
  micColorSwitchBase: {
    color: theme.pallet.micColor,
    '&$colorChecked': {
      color: theme.pallet.micColor,
      '& + $colorBar': {
        backgroundColor: theme.pallet.micColor,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class ChannelParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      RangeLabelWidth: 0,
      MapLabelWidth: 0,
      MicLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      RangeLabelWidth: ReactDOM.findDOMNode(this.RangeRef).offsetWidth,
      MapLabelWidth: ReactDOM.findDOMNode(this.MapRef).offsetWidth,
      MicLabelWidth: ReactDOM.findDOMNode(this.MicRef).offsetWidth,
    });
  }

  render() {
    const {
      activeChannels,
      channelRanges,
      channelMaps,
      onToggleChannel,
      onChangeChannelRange,
      onChangeChannelMap,
      classes,
    } = this.props;
    const { RangeLabelWidth, MapLabelWidth, MicLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Channel Parameters
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.ch1}
                onChange={onToggleChannel('ch1')}
                value={'CH1'}
                classes={{
                  switchBase: classes.ch1ColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH1"
          />
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              ref={ref => {
                this.RangeRef = ref;
              }}
              htmlFor="outlined-range-ch1"
            >
              Range
            </InputLabel>
            <Select
              value={channelRanges.ch1}
              onChange={onChangeChannelRange('ch1')}
              input={
                <OutlinedInput
                  labelWidth={RangeLabelWidth}
                  name="outlined-range-ch1"
                  id="outlined-range-ch1"
                />
              }
            >
              {Object.entries(options.Range1).map((item, index) => {
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
          >
            <InputLabel
              ref={ref => {
                this.MapRef = ref;
              }}
              htmlFor="outlined-map-ch1"
            >
              Mapped To
            </InputLabel>
            <Select
              value={channelMaps.ch1}
              onChange={onChangeChannelMap('ch1')}
              input={
                <OutlinedInput
                  labelWidth={MapLabelWidth}
                  name="outlined-map-ch1"
                  id="outlined-map-ch1"
                />
              }
            >
              {Object.entries(options.Map1).map((item, index) => {
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
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.ch2}
                onChange={onToggleChannel('ch2')}
                value={'ch2'}
                classes={{
                  switchBase: classes.ch2ColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH2"
          />
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel htmlFor="outlined-range-ch2">Range</InputLabel>
            <Select
              value={channelRanges.ch2}
              onChange={onChangeChannelRange('ch2')}
              input={
                <OutlinedInput
                  labelWidth={RangeLabelWidth}
                  name="outlined-range-ch2"
                  id="outlined-range-ch2"
                />
              }
            >
              {Object.entries(options.Range1).map((item, index) => {
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
          >
            <InputLabel htmlFor="outlined-map-ch2">Mapped To</InputLabel>
            <Select
              value={channelMaps.ch2}
              onChange={onChangeChannelMap('ch2')}
              input={
                <OutlinedInput
                  labelWidth={MapLabelWidth}
                  name="outlined-map-ch2"
                  id="outlined-map-ch2"
                />
              }
            >
              {Object.entries(options.Map1).map((item, index) => {
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
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.ch3}
                onChange={onToggleChannel('ch3')}
                value={'ch3'}
                classes={{
                  switchBase: classes.ch3ColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH3"
          />
        </OptionsRowWrapper>
        <OptionsRowWrapper>
          <FormControlLabel
            control={
              <Switch
                checked={activeChannels.mic}
                onChange={onToggleChannel('mic')}
                value={'mic'}
                classes={{
                  switchBase: classes.micColorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="MIC"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            disabled={!activeChannels.mic}
          >
            <InputLabel
              ref={ref => {
                this.MicRef = ref;
              }}
              htmlFor="outlined-map-mic"
            >
              Mic Type
            </InputLabel>
            <Select
              value={channelMaps.mic}
              onChange={onChangeChannelMap('mic')}
              input={
                <OutlinedInput
                  labelWidth={MicLabelWidth}
                  name="outlined-map-mic"
                  id="outlined-map-mic"
                />
              }
            >
              {Object.entries(options.Mic).map((item, index) => {
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

export default withTheme()(withStyles(styles)(ChannelParameters));
