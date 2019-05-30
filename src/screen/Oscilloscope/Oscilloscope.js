import React, { Component } from 'react';
import debounce from 'lodash/debounce';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import FFTGraph from './components/FFTGraph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class Oscilloscope extends Component {
  constructor(props) {
    super(props);
    this.timeBaseList = [0.5, 1, 5, 10, 20, 25, 50];
    this.state = {
      isReading: false,
      timeBaseIndex: 0,
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
        mic: 'Inbuilt',
      },
      isTriggerActive: false,
      triggerVoltage: 0,
      triggerChannel: 'CH1',
      isFourierTransformActive: false,
      transformType: 'Sine',
      transformChannel1: 'CH1',
      transformChannel2: 'CH2',
      isXYPlotActive: false,
      plotChannel1: 'CH1',
      plotChannel2: 'CH2',
    };
  }

  componentDidMount() {
    ipcRenderer.on('TO_RENDERER_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('TO_RENDERER_CONFIG', (event, args) => {
      const {
        timeBase,
        ch1,
        ch2,
        ch3,
        mic,
        ch1Map,
        ch2Map,
        micMap,
        isTriggerActive,
        triggerVoltage,
        triggerChannel,
        isFourierTransformActive,
        transformType,
        transformChannel1,
        transformChannel2,
        isXYPlotActive,
        plotChannel1,
        plotChannel2,
      } = args;
      this.setState({
        timeBaseIndex: this.timeBaseList.indexOf(timeBase),
        activeChannels: { ch1, ch2, ch3, mic },
        channelMaps: { ch1: ch1Map, ch2: ch2Map, mic: micMap },
        isTriggerActive,
        triggerVoltage,
        triggerChannel,
        isFourierTransformActive,
        transformType,
        transformChannel1,
        transformChannel2,
        isXYPlotActive,
        plotChannel1,
        plotChannel2,
      });
    });
    this.getConfigFromDevice();
  }

  componentWillUnmount() {
    const { isReading } = this.state;
    isReading &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'STOP_OSC',
      });
    ipcRenderer.removeAllListeners('TO_RENDERER_CONFIG');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_OSC',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    const {
      timeBaseIndex,
      activeChannels,
      isTriggerActive,
      triggerVoltage,
      triggerChannel,
      isFourierTransformActive,
    } = this.state;
    isConnected &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_OSC',
        timeBase: this.timeBaseList[timeBaseIndex],
        numberOfSamples: 1000,
        ch1: activeChannels.ch1,
        ch2: activeChannels.ch2,
        ch3: activeChannels.ch3,
        mic: activeChannels.mic,
        isTriggerActive,
        triggerVoltage,
        triggerChannel,
        isFourierTransformActive,
      });
  }, 500);

  onToggleRead = event => {
    const { isReading } = this.state;
    this.setState(prevState => ({
      isReading: !prevState.isReading,
    }));
    if (isReading) {
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'STOP_OSC',
      });
    } else {
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'START_OSC',
      });
    }
  };

  onToggleChannel = channelName => event => {
    this.setState(
      prevState => ({
        activeChannels: {
          ...prevState.activeChannels,
          [channelName]: !prevState.activeChannels[channelName],
        },
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };
  onChangeChannelRange = channelName => event => {
    this.setState(prevState => ({
      channelRanges: {
        ...prevState.channelRanges,
        [channelName]: event.target.value,
      },
    }));
  };
  onChangeChannelMap = channelName => event => {
    this.setState(prevState => ({
      channelMaps: {
        ...prevState.channelMaps,
        [channelName]: event.target.value,
      },
    }));
  };

  onToggleCheckBox = type => event => {
    let { isFourierTransformActive, isXYPlotActive } = this.state;
    if (type === 'isFourierTransformActive') {
      isFourierTransformActive = !isFourierTransformActive;
      isXYPlotActive = false;
    } else if (type === 'isXYPlotActive') {
      isFourierTransformActive = false;
      isXYPlotActive = !isXYPlotActive;
    }

    this.setState(
      prevState => ({
        [type]: !prevState[type],
        isFourierTransformActive,
        isXYPlotActive,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onChangeTriggerVoltage = (event, value) => {
    this.setState(
      prevState => ({
        triggerVoltage: value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };
  onChangeTriggerChannel = event => {
    this.setState(
      prevState => ({
        triggerChannel: event.target.value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };
  onChangeTimeBaseIndex = (event, value) => {
    this.setState(
      prevState => ({
        timeBaseIndex: value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onChangeTransformType = event => {
    this.setState(prevState => ({
      transformType: event.target.value,
    }));
  };
  onChangeTransformChannel = channelNumber => event => {
    this.setState(prevState => ({
      [channelNumber]: event.target.value,
    }));
  };

  onChangePlotChannel = channelNumber => event => {
    this.setState(prevState => ({
      [channelNumber]: event.target.value,
    }));
  };

  graphRenderer = () => {
    const {
      timeBaseIndex,
      activeChannels,
      channelRanges,
      isFourierTransformActive,
      isXYPlotActive,
    } = this.state;
    if (isFourierTransformActive) {
      return <FFTGraph activeChannels={activeChannels} />;
    }
    if (isXYPlotActive) {
      // return XY plot graph
    }
    return (
      <Graph
        channelRanges={channelRanges}
        activeChannels={activeChannels}
        timeBase={this.timeBaseList[timeBaseIndex]}
      />
    );
  };

  render() {
    const {
      isReading,
      timeBaseIndex,
      activeChannels,
      channelRanges,
      channelMaps,
      isTriggerActive,
      triggerVoltage,
      triggerChannel,
      isFourierTransformActive,
      transformType,
      transformChannel1,
      transformChannel2,
      isXYPlotActive,
      plotChannel1,
      plotChannel2,
    } = this.state;
    const { isConnected } = this.props;
    return (
      <GraphPanelLayout
        settings={
          <Settings
            timeBaseIndex={timeBaseIndex}
            timeBase={this.timeBaseList[timeBaseIndex]}
            activeChannels={activeChannels}
            channelRanges={channelRanges}
            isTriggerActive={isTriggerActive}
            channelMaps={channelMaps}
            triggerVoltage={triggerVoltage}
            triggerChannel={triggerChannel}
            isFourierTransformActive={isFourierTransformActive}
            transformType={transformType}
            transformChannel1={transformChannel1}
            transformChannel2={transformChannel2}
            isXYPlotActive={isXYPlotActive}
            plotChannel1={plotChannel1}
            plotChannel2={plotChannel2}
            onToggleChannel={this.onToggleChannel}
            onChangeChannelRange={this.onChangeChannelRange}
            onChangeChannelMap={this.onChangeChannelMap}
            onToggleCheckBox={this.onToggleCheckBox}
            onChangeTriggerVoltage={this.onChangeTriggerVoltage}
            onChangeTriggerChannel={this.onChangeTriggerChannel}
            onChangeTimeBaseIndex={this.onChangeTimeBaseIndex}
            timeBaseListLength={this.timeBaseList.length}
            onChangeTransformType={this.onChangeTransformType}
            onChangeTransformChannel={this.onChangeTransformChannel}
            onChangePlotChannel={this.onChangePlotChannel}
          />
        }
        actionButtons={
          <ActionButtons
            isConnected={isConnected}
            isReading={isReading}
            onToggleRead={this.onToggleRead}
          />
        }
        graph={this.graphRenderer()}
      />
    );
  }
}

export default Oscilloscope;
