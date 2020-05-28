import React, { Component } from 'react';
import { connect } from 'react-redux';
import SimplePanelLayout from '../../components/SimplePanelLayout';
import InstrumentCluster from './components/InstrumentCluster';
import debounce from 'lodash/debounce';
import { optionMap } from './components/SettingOptions';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class Multimeter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isWriting: false,
      isReading: false,
      unit: 'V',
      activeCategory: 'VOLTAGE',
      activeSubType: 'CH1',
      parameter: 'PULSE_FREQUENCY',
      dialValue: 0,
    };
  }

  componentDidMount() {
    const { startRead, stopRead } = this.props;
    ipcRenderer.on('CONNECTION_STATUS_MUL_MET', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
      isConnected ? startRead('START_MUL_MET') : stopRead('STOP_MUL_MET');
    });
    ipcRenderer.on('MUL_MET_CONFIG', (event, args) => {
      const { activeCategory, activeSubType, parameter } = args;
      const dialValue = optionMap[activeSubType].angle;
      const unit =
        activeCategory === 'PULSE'
          ? optionMap[activeSubType].unit[parameter]
          : optionMap[activeSubType].unit;
      this.setState({
        activeCategory,
        activeSubType,
        parameter,
        dialValue,
        unit,
      });
    });
    this.getConfigFromDevice();
    startRead('START_MUL_MET');
  }

  componentWillUnmount() {
    const { stopRead, stopWriting } = this.props;
    stopRead('STOP_MUL_MET');
    stopWriting();
    ipcRenderer.removeAllListeners('MUL_MET_CONFIG');
    ipcRenderer.removeAllListeners('CONNECTION_STATUS_MUL_MET');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_MUL_MET',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    const { activeCategory, activeSubType, parameter } = this.state;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_MUL_MET',
        activeCategory,
        activeSubType,
        parameter,
      });
  }, 500);

  onTogglePulseUnit = () => {
    let { activeSubType, parameter } = this.state;
    parameter =
      parameter === 'PULSE_FREQUENCY' ? 'PULSE_COUNT' : 'PULSE_FREQUENCY';
    const unit = optionMap[activeSubType].unit[parameter];
    this.setState(
      prevState => ({
        parameter,
        unit,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onClickButton = activeSubType => () => {
    this.changeOption(activeSubType);
  };

  changeDialValue = dialValue => {
    this.setState({
      dialValue,
    });
  };

  changeOption = activeSubType => {
    const { parameter } = this.state;
    const activeCategory = optionMap[activeSubType].category;
    const dialValue = optionMap[activeSubType].angle;
    const unit =
      activeCategory === 'PULSE'
        ? optionMap[activeSubType].unit[parameter]
        : optionMap[activeSubType].unit;
    this.setState(
      {
        data: 0,
        activeCategory,
        activeSubType,
        parameter,
        dialValue,
        unit,
      },
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  render() {
    const { activeSubType, data, unit, dialValue, activeCategory } = this.state;
    const { isReading } = this.props;
    return (
      <SimplePanelLayout
        panel={
          <InstrumentCluster
            activeSubType={activeSubType}
            onClickButton={this.onClickButton}
            changeOption={this.changeOption}
            changeDialValue={this.changeDialValue}
            onTogglePulseUnit={this.onTogglePulseUnit}
            isReading={isReading}
            data={data}
            unit={unit}
            dialValue={dialValue}
            activeCategory={activeCategory}
          />
        }
      />
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default connect(mapStateToProps, null)(Multimeter);
