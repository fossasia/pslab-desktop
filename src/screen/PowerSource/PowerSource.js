import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
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
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('PWR_SRC_CONFIG', (event, args) => {
      const { pv1, pv2, pv3, pcs } = args;
      this.setState({
        pv1: roundOff(pv1),
        pv2: roundOff(pv2),
        pv3: roundOff(pv3),
        pcs: roundOff(pcs),
      });
    });

    const { filePath } = this.props.match.params;
    filePath ? this.getConfigFromFile() : this.getConfigFromDevice();
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('PWR_SRC_CONFIG');
  }

  getConfigFromFile = debounce(() => {
    const { filePath } = this.props.match.params;
    const { isConnected, dataPath } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_PWR_SRC_FILE',
        dataPath: `${dataPath}/${filePath}`,
      });
  }, 500);

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_PWR_SRC',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
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
          />
        }
      />
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default withRouter(connect(mapStateToProps, null)(PowerSouce));
