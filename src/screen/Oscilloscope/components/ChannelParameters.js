import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {
  Checkbox,
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
    margin: '0px 16px 0px 0px',
  },
  ch1colorSwitchBase: {
    color: theme.pallet.ch1Color,
    '&$colorChecked': {
      color: theme.pallet.ch1Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.ch1Color,
      },
    },
  },
  ch2colorSwitchBase: {
    color: theme.pallet.ch2Color,
    '&$colorChecked': {
      color: theme.pallet.ch2Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.ch2Color,
      },
    },
  },
  ch3colorSwitchBase: {
    color: theme.pallet.ch3Color,
    '&$colorChecked': {
      color: theme.pallet.ch3Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.ch3Color,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
  ch2Switch: {
    color: theme.ch2Color,
  },
  ch3Switch: {
    color: theme.ch3Color,
  },
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
      isMicActive,
      onToggleCheckBox,
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
                  switchBase: classes.ch1colorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH1"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
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
                  switchBase: classes.ch2colorSwitchBase,
                  checked: classes.colorChecked,
                  bar: classes.colorBar,
                }}
              />
            }
            label="CH2"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
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
                  switchBase: classes.ch3colorSwitchBase,
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
              <Checkbox
                checked={isMicActive}
                onChange={onToggleCheckBox('isMicActive')}
              />
            }
            label="Mic"
          />
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
            disabled={!isMicActive}
          >
            <InputLabel
              ref={ref => {
                this.MicRef = ref;
              }}
              htmlFor="outlined-mic-ch3"
            >
              Mic Type
            </InputLabel>
            <Select
              value={channelMaps.ch4}
              onChange={onChangeChannelMap('ch4')}
              input={
                <OutlinedInput
                  labelWidth={MicLabelWidth}
                  name="outlined-mic-ch3"
                  id="outlined-mic-ch3"
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
