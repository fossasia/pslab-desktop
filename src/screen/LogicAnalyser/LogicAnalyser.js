import React, { Component } from 'react';
import { connect } from 'react-redux';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';

class LogicAnalyser extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isReading: false,
      numberOfChannels: 1,
      channel1Map: 'ID1',
      channel2Map: 'ID2',
      trigger1Type: 0,
      trigger2Type: 0,
      trigger3Type: 0,
      trigger4Type: 0,
      timeMeasureChannel1: 'ID1',
      timeMeasureChannel2: 'ID2',
      timeMeasuretrigger1Type: 1,
      timeMeasuretrigger2Type: 1,
      timeMeasureWrite1: 1,
      timeMeasureWrite2: 2,
      timeout: 10,
    };
  }

  componentDidMount() {}

  componentWillUnmount() {}

  toggleRead = () => {
    this.setState(prevState => ({ isReading: !prevState.isReading }));
  };

  changeNumberOfChannels = event => {
    this.setState({
      numberOfChannels: event.target.value,
    });
  };
  changeChannelMap = channelName => event => {
    this.setState({
      [channelName]: event.target.value,
    });
  };
  changeTriggerType = triggerNumber => event => {
    this.setState({
      [triggerNumber]: event.target.value,
    });
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
          <Graph isReading={isReading} numberOfChannels={numberOfChannels} />
        }
      />
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default connect(
  mapStateToProps,
  null,
)(LogicAnalyser);
