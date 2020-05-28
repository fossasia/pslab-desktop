import React, { Component } from 'react';
import { connect } from 'react-redux';
import debounce from 'lodash/debounce';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import FFTGraph from './components/FFTGraph';
import FitPanel from './components/FitPanel';
import XYPlotGraph from './components/XYPlotGraph';
import Settings from './components/Settings';
import roundOff from '../../utils/arithmetics';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class Oscilloscope extends Component {
  constructor(props) {
    super(props);
    this.timeBaseList = [0.5, 1, 5, 10, 20, 25, 50];
    this.state = {
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
      fitType: 'Sine',
      fitChannel1: 'None',
      fitChannel2: 'None',
      isXYPlotActive: false,
      plotChannel1: 'CH1',
      plotChannel2: 'CH2',
    };
  }

  componentDidMount() {
    const { startRead, stopRead } = this.props;
    ipcRenderer.on('CONNECTION_STATUS_OSC', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
      isConnected ? startRead('START_OSC') : stopRead('STOP_OSC');
    });
    ipcRenderer.on('OSC_CONFIG', (event, args) => {
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
        fitType,
        fitChannel1,
        fitChannel2,
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
        fitType,
        fitChannel1,
        fitChannel2,
        isXYPlotActive,
        plotChannel1,
        plotChannel2,
      });
    });
    this.getConfigFromDevice();
    startRead('START_OSC');
  }

  componentWillUnmount() {
    const { stopRead, stopWriting } = this.props;
    stopRead('STOP_OSC');
    stopWriting();
    ipcRenderer.removeAllListeners('OSC_CONFIG');
    ipcRenderer.removeAllListeners('CONNECTION_STATUS_OSC');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
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
      fitType,
      fitChannel1,
      fitChannel2,
      isXYPlotActive,
      plotChannel1,
      plotChannel2,
    } = this.state;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
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
        fitType,
        fitChannel1,
        fitChannel2,
        isXYPlotActive,
        plotChannel1,
        plotChannel2,
      });
  }, 500);

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
        triggerVoltage: roundOff(value),
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

  onChangeFitType = event => {
    this.setState(
      prevState => ({
        fitType: event.target.value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };
  onChangeFitChannel = channelNumber => event => {
    this.setState(
      prevState => ({
        [channelNumber]: event.target.value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onChangePlotChannel = channelNumber => event => {
    this.setState(
      prevState => ({
        [channelNumber]: event.target.value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  graphRenderer = () => {
    const {
      timeBaseIndex,
      activeChannels,
      channelRanges,
      isFourierTransformActive,
      isXYPlotActive,
      plotChannel1,
      plotChannel2,
    } = this.state;
    const { isReading } = this.props;
    if (isFourierTransformActive) {
      return <FFTGraph isReading={isReading} activeChannels={activeChannels} />;
    }
    if (isXYPlotActive) {
      return (
        <XYPlotGraph
          isReading={isReading}
          activeChannels={activeChannels}
          plotChannel1={plotChannel1}
          plotChannel2={plotChannel2}
        />
      );
    }
    return (
      <Graph
        isReading={isReading}
        channelRanges={channelRanges}
        activeChannels={activeChannels}
        timeBase={this.timeBaseList[timeBaseIndex]}
      />
    );
  };

  render() {
    const {
      timeBaseIndex,
      activeChannels,
      channelRanges,
      channelMaps,
      isTriggerActive,
      triggerVoltage,
      triggerChannel,
      isFourierTransformActive,
      fitType,
      fitChannel1,
      fitChannel2,
      isXYPlotActive,
      plotChannel1,
      plotChannel2,
    } = this.state;
    const { isReading } = this.props;
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
            fitType={fitType}
            fitChannel1={fitChannel1}
            fitChannel2={fitChannel2}
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
            onChangeFitType={this.onChangeFitType}
            onChangeFitChannel={this.onChangeFitChannel}
            onChangePlotChannel={this.onChangePlotChannel}
          />
        }
        graph={this.graphRenderer()}
        information={
          (fitChannel1 !== 'None' || fitChannel2 !== 'None') &&
          isFourierTransformActive && (
            <FitPanel
              isReading={isReading}
              fitType={fitType}
              fitChannel1={fitChannel1}
              fitChannel2={fitChannel2}
            />
          )
        }
      />
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default connect(mapStateToProps, null)(Oscilloscope);
