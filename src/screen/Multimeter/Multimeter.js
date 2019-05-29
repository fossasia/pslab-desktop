import React, { Component } from 'react';
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
      isReading: false,
      prefix: null,
      data: 0,
      unit: 'V',
      activeCatagory: 'VOLTAGE',
      activeSubType: 'CH1',
      parameter: 'PULSE_FREQUENCY',
      dialValue: 0,
    };
  }

  componentDidMount() {
    ipcRenderer.on('TO_RENDERER_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('TO_RENDERER_DATA', (event, args) => {
      this.setState({
        ...args,
      });
    });
    ipcRenderer.on('TO_RENDERER_CONFIG', (event, args) => {
      const { activeCatagory, activeSubType, parameter } = args;
      const dialValue = optionMap[activeSubType].angle;
      const unit =
        activeCatagory === 'PULSE'
          ? optionMap[activeSubType].unit[parameter]
          : optionMap[activeSubType].unit;
      this.setState({
        activeCatagory,
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
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'STOP_MUL_MET',
      });
    ipcRenderer.removeAllListeners('TO_RENDERER_DATA');
    ipcRenderer.removeAllListeners('TO_RENDERER_CONFIG');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_MUL_MET',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    const { activeCatagory, activeSubType, parameter } = this.state;
    console.log(activeCatagory, activeSubType, parameter);
    isConnected &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_MUL_MET',
        activeCatagory,
        activeSubType,
        parameter,
      });
  }, 500);

  onToggleRead = event => {
    const { isReading } = this.state;
    this.setState(prevState => ({
      isReading: !prevState.isReading,
    }));
    if (isReading) {
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'STOP_MUL_MET',
      });
    } else {
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'START_MUL_MET',
      });
    }
  };

  onClickButton = activeSubType => () => {
    this.changeOption(activeSubType);
  };

  changeOption = activeSubType => {
    const { parameter } = this.state;
    const activeCatagory = optionMap[activeSubType].catagory;
    const dialValue = optionMap[activeSubType].angle;
    const unit =
      activeCatagory === 'PULSE'
        ? optionMap[activeSubType].unit[parameter]
        : optionMap[activeSubType].unit;
    this.setState(
      {
        data: 0,
        activeCatagory,
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
    const { activeSubType, data, unit, dialValue, isReading } = this.state;
    const { isConnected } = this.props;
    return (
      <SimplePanelLayout
        panel={
          <InstrumentCluster
            activeSubType={activeSubType}
            onClickButton={this.onClickButton}
            changeOption={this.changeOption}
            onToggleRead={this.onToggleRead}
            isReading={isReading}
            data={data}
            unit={unit}
            dialValue={dialValue}
            isConnected={isConnected}
          />
        }
      />
    );
  }
}

export default Multimeter;
