import {
  TOGGLE_READ,
  TOGGLE_CHANNEL,
  CHANGE_CHANNEL_RANGE,
  CHANGE_CHANNEL_MAP,
  TOGGLE_TRIGGER,
  CHANGE_TRIGGER_VOLTAGE,
  CHANGE_TRIGGER_CHANNEL,
  CHANGE_TIME_BASE_INDEX,
  TOGGLE_FOURIER_TRANSFORM,
  CHANGE_FIT_TYPE,
  CHANGE_FIT_CHANNEL,
  TOGGLE_XY_PLOT,
  CHANGE_PLOT_CHANNEL,
} from '../actionTypes/oscilloscope';

export const toggleRead = () => {
  return {
    type: TOGGLE_READ,
  };
};

export const toggleChannel = ({ channelName }) => {
  return {
    type: TOGGLE_CHANNEL,
    payload: { channelName },
  };
};

export const changeChannelRange = ({ channelName, value }) => {
  return {
    type: CHANGE_CHANNEL_RANGE,
    payload: { channelName, value },
  };
};

export const changeChannelMap = ({ channelName, value }) => {
  return {
    type: CHANGE_CHANNEL_MAP,
    payload: { channelName, value },
  };
};

export const toggleTrigger = () => {
  return {
    type: TOGGLE_TRIGGER,
  };
};

export const changeTriggerVoltage = ({ value }) => {
  return {
    type: CHANGE_TRIGGER_VOLTAGE,
    payload: { value },
  };
};

export const changeTriggerChannel = ({ value }) => {
  return {
    type: CHANGE_TRIGGER_CHANNEL,
    payload: { value },
  };
};

export const ChangeTimeBaseIndex = ({ index, value }) => {
  return {
    type: CHANGE_TIME_BASE_INDEX,
    payload: { index, value },
  };
};

export const toggleFourierTransform = () => {
  return {
    type: TOGGLE_FOURIER_TRANSFORM,
  };
};

export const changeFitType = ({ value }) => {
  return {
    type: CHANGE_FIT_TYPE,
    payload: { value },
  };
};

export const changeFitChannel = ({ channelNumber, value }) => {
  return {
    type: CHANGE_FIT_CHANNEL,
    payload: { channelNumber, value },
  };
};

export const toggleXYPlot = () => {
  return {
    type: TOGGLE_XY_PLOT,
  };
};

export const changePlotChannel = ({ channelNumber, value }) => {
  return {
    type: CHANGE_PLOT_CHANNEL,
    payload: { channelNumber, value },
  };
};
