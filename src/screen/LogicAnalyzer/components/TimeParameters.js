import React, { Component } from 'react';
import { Typography, Divider } from '@material-ui/core';
import CustomSliderInput from '../../../components/CustomSliderInput';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';

class TimeParameters extends Component {
  render() {
    const {
      captureTimeListLength,
      captureTimeIndex,
      captureTime,
      onChangeCaptureTimeIndex,
    } = this.props;
    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Capture Time
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <CustomSliderInput
            title="captureTime"
            unit="ms"
            onChangeSlider={onChangeCaptureTimeIndex}
            value={captureTimeIndex}
            min={0}
            max={captureTimeListLength - 1}
            step={1}
            minTitleWidth="60px"
            minUnitWidth="66px"
            display={captureTime}
          />
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}
export default TimeParameters;
