import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import debounce from 'lodash/debounce';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import FFTGraph from './components/FFTGraph';
import FitPanel from './components/FitPanel';
import XYPlotGraph from './components/XYPlotGraph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

const Oscilloscope = ({
  isConnected,
  activeChannels,
  channelRanges,
  channelMaps,
  isTriggerActive,
  triggerVoltage,
  triggerChannel,
  timeBaseIndex,
  timeBase,
  isFourierTransformActive,
  fitType,
  fitChannel1,
  fitChannel2,
  isXYPlotActive,
  plotChannel1,
  plotChannel2,
}) => {
  useEffect(() => {
    isConnected && sendConfigToDevice();
  }, [
    activeChannels,
    channelRanges,
    channelMaps,
    isTriggerActive,
    triggerVoltage,
    triggerChannel,
    timeBaseIndex,
    timeBase,
    isFourierTransformActive,
    fitType,
    fitChannel1,
    fitChannel2,
    isXYPlotActive,
    plotChannel1,
    plotChannel2,
  ]);

  const sendConfigToDevice = debounce(() => {
    loadBalancer.sendData(ipcRenderer, 'linker', {
      command: 'SET_CONFIG_OSC',
      ch1: activeChannels.ch1,
      ch2: activeChannels.ch2,
      ch3: activeChannels.ch3,
      mic: activeChannels.mic,
      isTriggerActive,
      triggerVoltage,
      triggerChannel,
      timeBase,
      isFourierTransformActive,
      fitType,
      fitChannel1,
      fitChannel2,
      isXYPlotActive,
      plotChannel1,
      plotChannel2,
    });
  }, 250);

  const graphRenderer = () => {
    if (isFourierTransformActive) {
      return <FFTGraph />;
    }
    if (isXYPlotActive) {
      return <XYPlotGraph />;
    }
    return <Graph />;
  };

  const fitPanelRenderer = () => {
    return (
      (fitChannel1 !== 'None' || fitChannel2 !== 'None') &&
      isFourierTransformActive && <FitPanel />
    );
  };

  return (
    <GraphPanelLayout
      settings={<Settings />}
      actionButtons={<ActionButtons />}
      graph={graphRenderer()}
      information={fitPanelRenderer()}
    />
  );
};

const mapStateToProps = state => {
  const {
    activeChannels,
    channelRanges,
    channelMaps,
    isTriggerActive,
    triggerVoltage,
    triggerChannel,
    timeBaseIndex,
    timeBase,
    isFourierTransformActive,
    fitType,
    fitChannel1,
    fitChannel2,
    isXYPlotActive,
    plotChannel1,
    plotChannel2,
  } = state.oscilloscope;
  const { isConnected } = state.app.device;
  return {
    isConnected,
    activeChannels,
    channelRanges,
    channelMaps,
    isTriggerActive,
    triggerVoltage,
    triggerChannel,
    timeBaseIndex,
    timeBase,
    isFourierTransformActive,
    fitType,
    fitChannel1,
    fitChannel2,
    isXYPlotActive,
    plotChannel1,
    plotChannel2,
  };
};

export default connect(
  mapStateToProps,
  null,
)(Oscilloscope);
