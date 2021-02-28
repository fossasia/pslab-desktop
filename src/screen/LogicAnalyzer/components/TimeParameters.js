import React, { Component } from 'react';
import { Typography, Divider } from '@material-ui/core';
import CustomSliderInput from '../../../components/CustomSliderInput';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';

const inputCheck = value => {
  let regex = /(^([0-9]+([.][0-9]*)?|[.][0-9]+)$|^$)/; // non-negative float or blank
  return regex.test(value);
};

class TimeParameters extends Component {
  render() {
    const { onChangeCaptureTime, captureTime, maxCaptureTime } = this.props;
    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Capture Time
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <CustomSliderInput
            title="captureTime"
            unit="μs"
            onChangeSlider={onChangeCaptureTime}
            value={captureTime * 1e3} // convert ms to μs
            min={10}
            max={maxCaptureTime * 1e3} // convert ms to μs
            inputCheck={inputCheck}
            step={10}
            minTitleWidth="60px"
            minUnitWidth="66px"
          />
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}
export default TimeParameters;
