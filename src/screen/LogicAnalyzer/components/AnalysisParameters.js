import React, { Component } from 'react';
import {
  Select,
  Typography,
  Divider,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
  Table,
  TableHead,
  TableBody,
  TableCell,
  TableRow,
} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import CustomSliderInput from '../../../components/CustomSliderInput';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';
import formStyles from '../../utils/formStyles';

class AnalysisParameters extends Component {
  render() {
    const {
      timeMeasureChannel1,
      timeMeasureChannel2,
      timeMeasuretrigger1Type,
      timeMeasuretrigger2Type,
      timeMeasureWrite1,
      timeMeasureWrite2,
      timeout,
      changeTimeMeasureChannel,
      changeTimeMeasureTriggerType,
      changeTimeMeasureWrite,
      changeTimeout,
      classes,
    } = this.props;
    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Analysis Parameters
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel className={classes.label} htmlFor="outlined-channel1">
              Channel 1
            </InputLabel>
            <Select
              value={timeMeasureChannel1}
              onChange={changeTimeMeasureChannel('timeMeasureChannel1')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-channel1"
                  id="outlined-channel1"
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
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel className={classes.label} htmlFor="outlined-trigger1">
              Trigger Type
            </InputLabel>
            <Select
              value={timeMeasuretrigger1Type}
              onChange={changeTimeMeasureTriggerType('timeMeasuretrigger1Type')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-trigger1"
                  id="outlined-trigger1"
                />
              }
            >
              {Object.entries(options.TimeMeasureTrigger).map((item, index) => {
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
            <InputLabel className={classes.label} htmlFor="outlined-write1">
              Write To
            </InputLabel>
            <Select
              value={timeMeasureWrite1}
              onChange={changeTimeMeasureWrite('timeMeasureWrite1')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-write1"
                  id="outlined-write1"
                />
              }
            >
              {Object.entries(options.Write).map((item, index) => {
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
        <Divider />
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel className={classes.label} htmlFor="outlined-channel2">
              Channel 1
            </InputLabel>
            <Select
              value={timeMeasureChannel2}
              onChange={changeTimeMeasureChannel('timeMeasureChannel2')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-channel2"
                  id="outlined-channel2"
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
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel className={classes.label} htmlFor="outlined-trigger2">
              Trigger Type
            </InputLabel>
            <Select
              value={timeMeasuretrigger2Type}
              onChange={changeTimeMeasureTriggerType('timeMeasuretrigger2Type')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-trigger2"
                  id="outlined-trigger2"
                />
              }
            >
              {Object.entries(options.TimeMeasureTrigger).map((item, index) => {
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
            <InputLabel className={classes.label} htmlFor="outlined-write2">
              Write To
            </InputLabel>
            <Select
              value={timeMeasureWrite2}
              onChange={changeTimeMeasureWrite('timeMeasureWrite2')}
              input={
                <OutlinedInput
                  labelWidth={0}
                  name="outlined-write2"
                  id="outlined-write2"
                />
              }
            >
              {Object.entries(options.Write).map((item, index) => {
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
        <Divider />
        <OptionsRowWrapper>
          <CustomSliderInput
            title="Timeout"
            unit="mSec"
            onChangeSlider={changeTimeout}
            value={timeout}
            min={10}
            max={10000}
            step={1}
            minTitleWidth="48px"
            minUnitWidth="60px"
          />
        </OptionsRowWrapper>
        <Divider />
        <OptionsRowWrapper>
          <Table size="small" padding="dense">
            <TableHead>
              <TableRow>
                <TableCell>Index</TableCell>
                <TableCell align="right">Time (mSec)</TableCell>
                <TableCell align="right">Time (mSec)</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow>
                <TableCell component="th" scope="row">
                  1
                </TableCell>
                <TableCell align="right">--/-</TableCell>
                <TableCell align="right">--/-</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">
                  2
                </TableCell>
                <TableCell align="right">--/-</TableCell>
                <TableCell align="right">--/-</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">
                  3
                </TableCell>
                <TableCell align="right">--/-</TableCell>
                <TableCell align="right">--/-</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">
                  4
                </TableCell>
                <TableCell align="right">--/-</TableCell>
                <TableCell align="right">--/-</TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}

export default withStyles(formStyles)(AnalysisParameters);
