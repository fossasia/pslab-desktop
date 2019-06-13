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

const initialState = {
  isReading: false,
  activeChannels: {
    ch1: true,
    ch2: false,
    ch3: false,
    mic: false,
  },
  channelRanges: {
    ch1: '8',
    ch2: '8',
    ch3: '3',
  },
  channelMaps: {
    ch1: 'CH1',
    ch2: 'CH2',
  },
  isTriggerActive: false,
  triggerVoltage: 0,
  triggerChannel: 'CH1',
  timeBaseIndex: 0,
  timeBase: 0.5,
  isFourierTransformActive: false,
  fitType: 'Sine',
  fitChannel1: 'None',
  fitChannel2: 'None',
  isXYPlotActive: false,
  plotChannel1: 'CH1',
  plotChannel2: 'CH2',
};

export const oscilloscopeReducer = (prevState = initialState, action) => {
  switch (action.type) {
    case TOGGLE_READ: {
      return { ...prevState, isReading: !prevState.isReading };
    }
    case TOGGLE_CHANNEL: {
      const { channelName } = action.payload;
      return {
        ...prevState,
        activeChannels: {
          ...prevState.activeChannels,
          [channelName]: !prevState.activeChannels[channelName],
        },
      };
    }
    case CHANGE_CHANNEL_RANGE: {
      const { channelName, value } = action.payload;
      return {
        ...prevState,
        channelRanges: {
          ...prevState.channelRanges,
          [channelName]: value,
        },
      };
    }
    case CHANGE_CHANNEL_MAP: {
      const { channelName, value } = action.payload;
      return {
        ...prevState,
        channelMaps: {
          ...prevState.channelMaps,
          [channelName]: value,
        },
      };
    }
    case TOGGLE_TRIGGER: {
      return { ...prevState, isTriggerActive: !prevState.isTriggerActive };
    }
    case CHANGE_TRIGGER_VOLTAGE: {
      const { value } = action.payload;
      return { ...prevState, triggerVoltage: value };
    }
    case CHANGE_TRIGGER_CHANNEL: {
      const { value } = action.payload;
      return { ...prevState, triggerChannel: value };
    }
    case CHANGE_TIME_BASE_INDEX: {
      const { index, value } = action.payload;
      return { ...prevState, timeBaseIndex: index, timeBase: value };
    }
    case TOGGLE_FOURIER_TRANSFORM: {
      return {
        ...prevState,
        isFourierTransformActive: !prevState.isFourierTransformActive,
        isXYPlotActive: false,
      };
    }
    case CHANGE_FIT_TYPE: {
      const { value } = action.payload;
      return { ...prevState, fitType: value };
    }
    case CHANGE_FIT_CHANNEL: {
      const { channelNumber, value } = action.payload;
      return { ...prevState, [channelNumber]: value };
    }
    case TOGGLE_XY_PLOT: {
      return {
        ...prevState,
        isXYPlotActive: !prevState.isXYPlotActive,
        isFourierTransformActive: false,
      };
    }
    case CHANGE_PLOT_CHANNEL: {
      const { channelNumber, value } = action.payload;
      return { ...prevState, [channelNumber]: value };
    }
    default:
      return prevState;
  }
};
