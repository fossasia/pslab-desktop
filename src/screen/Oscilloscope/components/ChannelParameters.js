import React, { useState, useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
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
import {
  toggleChannel,
  changeChannelRange,
  changeChannelMap,
} from '../../../redux/actions/oscilloscope';

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

const ChannelParameters = ({
  activeChannels,
  channelRanges,
  channelMaps,
  toggleChannel,
  changeChannelRange,
  changeChannelMap,
  classes,
}) => {
  let ref = {
    range: useRef(),
    map: useRef(),
  };

  const [width, setWidth] = useState({
    range: 0,
    map: 0,
  });

  useEffect(() => {
    setWidth({
      range: ReactDOM.findDOMNode(ref.range).offsetWidth,
      map: ReactDOM.findDOMNode(ref.map).offsetWidth,
    });
  }, []);

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
              onChange={() => toggleChannel({ channelName: 'ch1' })}
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
            ref={DOMref => {
              ref.range = DOMref;
            }}
            htmlFor="outlined-range-ch1"
          >
            Range
          </InputLabel>
          <Select
            value={channelRanges.ch1}
            onChange={event =>
              changeChannelRange({
                channelName: 'ch1',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.range}
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
            ref={DOMref => {
              ref.map = DOMref;
            }}
            htmlFor="outlined-map-ch1"
          >
            Mapped To
          </InputLabel>
          <Select
            value={channelMaps.ch1}
            onChange={event =>
              changeChannelMap({
                channelName: 'ch1',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.map}
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
              onChange={() => toggleChannel({ channelName: 'ch2' })}
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
            onChange={event =>
              changeChannelRange({
                channelName: 'ch2',
                value: event.target.value,
              })
            }
            input={
              <OutlinedInput
                labelWidth={width.range}
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
            onChange={event => {
              changeChannelMap({
                channelName: 'ch2',
                value: event.target.value,
              });
            }}
            input={
              <OutlinedInput
                labelWidth={width.map}
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
              onChange={() => toggleChannel({ channelName: 'ch3' })}
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
              onChange={() => toggleChannel({ channelName: 'mic' })}
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
      </OptionsRowWrapper>
    </SettingsWrapper>
  );
};

const mapStateToProps = state => {
  const { activeChannels, channelRanges, channelMaps } = state.oscilloscope;
  return {
    activeChannels,
    channelRanges,
    channelMaps,
  };
};

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      toggleChannel,
      changeChannelRange,
      changeChannelMap,
    },
    dispatch,
  ),
});

export default withTheme()(
  withStyles(styles)(
    connect(
      mapStateToProps,
      mapDispatchToProps,
    )(ChannelParameters),
  ),
);
