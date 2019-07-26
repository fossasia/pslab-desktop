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
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
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
  }

  componentWillUnmount() {
    const { isReading } = this.state;
    isReading &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'STOP_MUL_MET',
      });
    ipcRenderer.removeAllListeners('MUL_MET_CONFIG');
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

  onToggleRead = event => {
    const { isReading } = this.state;
    if (isReading) {
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'STOP_MUL_MET',
      });
    } else {
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'START_MUL_MET',
      });
    }
    this.setState(prevState => ({
      isReading: !prevState.isReading,
    }));
  };

  onToggleWrite = event => {
    const { isWriting } = this.state;
    const { dataPath } = this.props;
    if (isWriting) {
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'STOP_WRITE',
      });
    } else {
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'START_WRITE',
        deviceType: 'Multimeter',
        dataPath: dataPath,
      });
    }
    this.setState(prevState => ({
      isWriting: !prevState.isWriting,
    }));
  };

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
    const {
      activeSubType,
      data,
      unit,
      dialValue,
      isWriting,
      isReading,
      activeCategory,
    } = this.state;
    const { isConnected } = this.props;
    return (
      <SimplePanelLayout
        panel={
          <InstrumentCluster
            activeSubType={activeSubType}
            onClickButton={this.onClickButton}
            changeOption={this.changeOption}
            changeDialValue={this.changeDialValue}
            onToggleRead={this.onToggleRead}
            onTogglePulseUnit={this.onTogglePulseUnit}
            isReading={isReading}
            data={data}
            unit={unit}
            dialValue={dialValue}
            isConnected={isConnected}
            activeCategory={activeCategory}
            isWriting={isWriting}
            onToggleWrite={this.onToggleWrite}
          />
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
)(Multimeter);
