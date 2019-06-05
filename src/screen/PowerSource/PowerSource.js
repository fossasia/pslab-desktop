import React, { Component } from 'react';
import SimplePanelLayout from '../../components/SimplePanelLayout';
import InstrumentCluster from './components/InstrumentCluster';
import roundOff from '../../utils/arithmetics';
import debounce from 'lodash/debounce';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class PowerSouce extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pv1: -5,
      pv2: -3.3,
      pv3: 0,
      pcs: 0,
    };
  }

  componentDidMount() {
    ipcRenderer.on('TO_RENDERER_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('TO_RENDERER_CONFIG', (event, args) => {
      const { pv1, pv2, pv3, pcs } = args;
      this.setState({
        pv1: roundOff(pv1),
        pv2: roundOff(pv2),
        pv3: roundOff(pv3),
        pcs: roundOff(pcs),
      });
    });
    this.getConfigFromDevice();
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('TO_RENDERER_CONFIG');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_PWR_SRC',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_PWR_SRC',
        ...this.state,
      });
  }, 500);

  onChangeSlider = pinType => value => {
    this.setState(
      {
        [pinType]: roundOff(parseFloat(value)),
      },
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onPressButton = (pinType, isPositive) => event => {
    this.setState(
      {
        [pinType]: roundOff(this.state[pinType] + (isPositive ? 0.01 : -0.01)),
      },
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  render() {
    const { pv1, pv2, pv3, pcs } = this.state;
    const { onOpenDialog } = this.props;

    return (
      <SimplePanelLayout
        panel={
          <InstrumentCluster
            pv1={pv1}
            pv2={pv2}
            pv3={pv3}
            pcs={pcs}
            onPressButton={this.onPressButton}
            onChangeSlider={this.onChangeSlider}
            onOpenDialog={onOpenDialog}
          />
        }
      />
    );
  }
}

export default PowerSouce;
