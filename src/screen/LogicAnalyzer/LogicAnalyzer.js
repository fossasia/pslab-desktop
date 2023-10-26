import React, { Component } from 'react';
import { connect } from 'react-redux';
import debounce from 'lodash/debounce';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class LogicAnalyzer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isReading: false,
      isAutoReading: true,
      numberOfChannels: 1,
      channel1Map: 'ID1',
      channel2Map: 'ID2',
      trigger1Type: 1,
      trigger2Type: 1,
      trigger3Type: 1,
      trigger4Type: 1,
      captureTime: 1, // ms
      maxCaptureTime: 1e3, // ms
    };
  }

  componentDidMount() {
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('LA_CONFIG', (event, args) => {
      const {
        captureTime,
        numberOfChannels,
        trigger1Type,
        trigger2Type,
        trigger3Type,
        trigger4Type,
      } = args;
      this.setState({
        captureTime,
        numberOfChannels,
        trigger1Type,
        trigger2Type,
        trigger3Type,
        trigger4Type,
      });
    });
    this.getConfigFromDevice();
  }

  componentWillUnmount() {
    const { isReading } = this.state;
    isReading &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'STOP_LA',
      });
    ipcRenderer.removeAllListeners('LA_CONFIG');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_LA',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    const {
      captureTime,
      numberOfChannels,
      trigger1Type,
      trigger2Type,
      trigger3Type,
      trigger4Type,
    } = this.state;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_LA',
        captureTime: captureTime,
        numberOfChannels,
        trigger1Type,
        trigger2Type,
        trigger3Type,
        trigger4Type,
      });
  }, 500);

  toggleRead = () => {
    const { isReading } = this.state;
    this.setState(prevState => ({ isReading: !prevState.isReading }));
    if (isReading) {
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'STOP_LA',
      });
    } else {
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'START_LA',
      });
    }
  };
  toggleAutoRead = () => {
    this.setState(prevState => ({ isAutoReading: !prevState.isAutoReading }));
  };

  changeNumberOfChannels = event => {
    this.setState(
      {
        numberOfChannels: event.target.value,
      },
      () => {
        this.sendConfigToDevice();
      },
    );
  };
  changeChannelMap = channelName => event => {
    this.setState({
      [channelName]: event.target.value,
    });
  };
  changeTriggerType = triggerNumber => event => {
    this.setState(
      {
        [triggerNumber]: event.target.value,
      },
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onChangeCaptureTime = (event, value) => {
    this.setState(
      () => ({
        captureTime: value / 1e3, // convert μs to ms
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };
  render() {
    const {
      isReading,
      isAutoReading,
      numberOfChannels,
      channel1Map,
      channel2Map,
      trigger1Type,
      trigger2Type,
      trigger3Type,
      trigger4Type,
      captureTime,
      maxCaptureTime,
    } = this.state;
    const { isConnected } = this.props;
    return (
      <GraphPanelLayout
        settings={
          <Settings
            numberOfChannels={numberOfChannels}
            channel1Map={channel1Map}
            channel2Map={channel2Map}
            trigger1Type={trigger1Type}
            trigger2Type={trigger2Type}
            trigger3Type={trigger3Type}
            trigger4Type={trigger4Type}
            changeNumberOfChannels={this.changeNumberOfChannels}
            changeChannelMap={this.changeChannelMap}
            changeTriggerType={this.changeTriggerType}
            onChangeCaptureTime={this.onChangeCaptureTime}
            captureTime={captureTime}
            maxCaptureTime={maxCaptureTime}
          />
        }
        actionButtons={
          <ActionButtons
            isConnected={isConnected}
            isReading={isReading}
            toggleRead={this.toggleRead}
            isAutoReading={isAutoReading}
            toggleAutoRead={this.toggleAutoRead}
          />
        }
        graph={
          <Graph
            isReading={isReading}
            toggleRead={this.toggleRead}
            isAutoReading={isAutoReading}
            numberOfChannels={numberOfChannels}
            dataPath={this.props.dataPath}
          />
        }
      />
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default connect(mapStateToProps, null)(LogicAnalyzer);
