import React, { Component } from 'react';
import SimplePanelLayout from '../../components/SimplePanelLayout';
import InstrumentCluster from './components/InstrumentCluster';
import debounce from 'lodash/debounce';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class Multimeter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isReading: false,
      data: 0,
      unit: 'V',
      activeCategory: 'VOLTAGE',
      activeSubType: 'CH1',
      parameter: null,
      dialValue: 0,
      ispulseSectionHz: true,
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
      this.setState({
        activeCatagory,
        activeSubType,
        parameter,
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
  onTogglePulseUnit = event => {
    let { ispulseSectionHz, unit, parameter } = this.state;
    if (!ispulseSectionHz) {
      unit = 'Hz';
      parameter = 'PULSE_FREQUENCY';
    } else {
      unit = 'xyz';
      parameter = 'PULSE_COUNT';
    }
    this.setState(prevState => ({
      ispulseSectionHz: !ispulseSectionHz,
      unit,
      parameter,
    }));
    this.sendConfigToDevice();
  };

  onClickButton = (
    optionName,
    unit,
    dialValue,
    activeCategory,
    parameter,
  ) => () => {
    this.setState(
      {
        activeSubType: optionName,
        unit,
        dialValue,
        data: 0,
        activeCategory,
        parameter,
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
      isReading,
      activeCategory,
      ispulseSectionHz,
    } = this.state;
    const { isConnected } = this.props;
    return (
      <SimplePanelLayout
        panel={
          <InstrumentCluster
            activeSubType={activeSubType}
            onClickButton={this.onClickButton}
            onChangeDial={this.onChangeDial}
            onToggleRead={this.onToggleRead}
            onTogglePulseUnit={this.onTogglePulseUnit}
            isReading={isReading}
            data={data}
            unit={unit}
            dialValue={dialValue}
            isConnected={isConnected}
            ispulseSectionHz={ispulseSectionHz}
            activeCategory={activeCategory}
          />
        }
      />
    );
  }
}

export default Multimeter;
