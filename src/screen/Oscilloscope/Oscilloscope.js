import React, { Component } from 'react';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class Oscilloscope extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isReading: false,
      data: [
        {
          ch1: 0,
          ch2: 0,
          ch3: 0,
          ch4: 0,
          timeGap: 0,
        },
      ],
      activeChannels: {
        ch1: true,
        ch2: true,
        ch3: false,
        ch4: false,
      },
      channelRanges: {
        ch1: '+/-8V',
        ch2: '+/-8V',
        ch3: '+/-8V',
        ch4: '+/-8V',
      },
      channelMaps: {
        ch1: 'CH1',
        ch2: 'Ch2',
        ch3: 'Ch3',
        ch4: 'CH4',
      },
      triggerVoltage: 5,
      timeBase: 100,
      triggerVoltageChannel: 'CH1',
      isTriggerActive: false,
      isFourierTransformActive: false,
      transformType: 'sin fit',
      transformChannel1: 'CH1',
      transformChannel2: 'CH2',
      isXYPlotActive: false,
      plotChannel1: 'CH1',
      plotChannel2: 'CH2',
    };
  }

  componentDidMount() {
    ipcRenderer.on('TO_RENDERER_DATA', (event, args) => {
      this.setState({
        data: args,
      });
    });
  }

  componentWillUnmount() {
    const { isReading } = this.state;
    isReading &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'STOP_OSC',
      });
    ipcRenderer.removeAllListeners('TO_RENDERER_DATA');
  }

  onToggleRead = event => {
    const { isReading, activeChannels } = this.state;
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
        timeGap: 10,
        numberOfSamples: 1000,
        delay: 30,
        ch1: activeChannels.ch1,
        ch2: activeChannels.ch2,
        ch3: activeChannels.ch3,
        ch4: activeChannels.ch4,
      });
    }
  };

  onToggleChannel = channelName => event => {
    console.log(event);
    this.setState(prevState => ({
      activeChannels: {
        ...prevState.activeChannels,
        [channelName]: event.target.checked,
      },
    }));
  };

  onChangeChannelRange = channelName => event => {
    this.setState(prevState => ({
      channelRanges: {
        ...prevState.channelRanges,
        [channelName]: event.target.checked,
      },
    }));
  };

  onChangeChannelMap = channelName => event => {
    this.setState(prevState => ({
      channelMaps: {
        ...prevState.channelMaps,
        [channelName]: event.target.checked,
      },
    }));
  };

  onToggleTrigger = () => {};
  onChangeTriggerVoltage = () => {};
  onChangeTriggerChannel = () => {};
  onChangeTimeBase = () => {};

  onTOggleFourierTransform = () => {};
  onChangeTransformType = () => {};
  onChangeTransformChannel = () => {};

  onChangePlotChannel = () => {};

  render() {
    const {
      data,
      isReading,
      activeChannels,
      channelRanges,
      channelMaps,
      triggerVoltage,
      timeBase,
      triggerVoltageChannel,
      isTriggerActive,
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
            onToggleChannel={this.onToggleChannel}
            onChangeChannelRange={this.onChangeChannelRange}
            onChangeChannelMap={this.onChangeChannelMap}
            channelRanges={channelRanges}
            activeChannels={activeChannels}
            channelMaps={channelMaps}
            triggerVoltage={triggerVoltage}
            timeBase={timeBase}
            triggerVoltageChannel={triggerVoltageChannel}
            isTriggerActive={isTriggerActive}
            isFourierTransformActive={isFourierTransformActive}
            transformType={transformType}
            transformChannel1={transformChannel1}
            transformChannel2={transformChannel2}
            onTOggleFourierTransform={this.onTOggleFourierTransform}
            onChangeTransformType={this.onChangeTransformType}
            onChangeTransformChannel={this.onChangeTransformChannel}
            isXYPlotActive={isXYPlotActive}
            plotChannel1={plotChannel1}
            plotChannel2={plotChannel2}
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
        graph={<Graph data={data} activeChannels={activeChannels} />}
      />
    );
  }
}

export default Oscilloscope;
