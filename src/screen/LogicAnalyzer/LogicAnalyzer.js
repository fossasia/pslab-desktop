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
      numberOfChannels: 1,
      channel1Map: 'ID1',
      channel2Map: 'ID2',
      trigger1Type: 1,
      trigger2Type: 1,
      trigger3Type: 1,
      trigger4Type: 1,
      timeMeasureChannel1: 'ID1',
      timeMeasureChannel2: 'ID2',
      timeMeasuretrigger1Type: 1,
      timeMeasuretrigger2Type: 1,
      timeMeasureWrite1: 1,
      timeMeasureWrite2: 2,
      timeout: 10,
    };
  }

  componentDidMount() {
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('LA_CONFIG', (event, args) => {
      const {
        numberOfChannels,
        trigger1Type,
        trigger2Type,
        trigger3Type,
        trigger4Type,
      } = args;
      this.setState({
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
      numberOfChannels,
      trigger1Type,
      trigger2Type,
      trigger3Type,
      trigger4Type,
    } = this.state;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_LA',
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

  changeTimeMeasureChannel = channelName => event => {
    this.setState({
      [channelName]: event.target.value,
    });
  };
  changeTimeMeasureTriggerType = triggerNumber => event => {
    this.setState({
      [triggerNumber]: event.target.value,
    });
  };
  changeTimeMeasureWrite = writeNumber => event => {
    this.setState({
      [writeNumber]: event.target.value,
    });
  };
  changeTimeout = (event, value) => {
    this.setState({
      timeout: value,
    });
  };

  render() {
    const {
      isReading,
      numberOfChannels,
      channel1Map,
      channel2Map,
      trigger1Type,
      trigger2Type,
      trigger3Type,
      trigger4Type,
      timeMeasureChannel1,
      timeMeasureChannel2,
      timeMeasuretrigger1Type,
      timeMeasuretrigger2Type,
      timeMeasureWrite1,
      timeMeasureWrite2,
      timeout,
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
            timeMeasureChannel1={timeMeasureChannel1}
            timeMeasureChannel2={timeMeasureChannel2}
            timeMeasuretrigger1Type={timeMeasuretrigger1Type}
            timeMeasuretrigger2Type={timeMeasuretrigger2Type}
            timeMeasureWrite1={timeMeasureWrite1}
            timeMeasureWrite2={timeMeasureWrite2}
            timeout={timeout}
            changeNumberOfChannels={this.changeNumberOfChannels}
            changeChannelMap={this.changeChannelMap}
            changeTriggerType={this.changeTriggerType}
            changeTimeMeasureChannel={this.changeTimeMeasureChannel}
            changeTimeMeasureTriggerType={this.changeTimeMeasureTriggerType}
            changeTimeMeasureWrite={this.changeTimeMeasureWrite}
            changeTimeout={this.changeTimeout}
          />
        }
        actionButtons={
          <ActionButtons
            isConnected={isConnected}
            isReading={isReading}
            toggleRead={this.toggleRead}
          />
        }
        graph={
          <Graph
            isReading={isReading}
            numberOfChannels={numberOfChannels}
            toggleRead={this.toggleRead}
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
