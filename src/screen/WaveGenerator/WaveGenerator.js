import React, { Component } from 'react';
import debounce from 'lodash/debounce';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import Settings from './components/Settings';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class WaveGenerator extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activePreview: {
        s1: true,
        s2: true,
        sqr1: true,
        sqr2: true,
        sqr3: true,
        sqr4: true,
      },
      s1Frequency: 10,
      s2Frequency: 10,
      s2Phase: 0,
      sqr1Frequency: 0,
      sqr1DutyCycle: 0,
      sqr2Frequency: 0,
      sqr2DutyCycle: 0,
      sqr2Phase: 0,
      sqr3Frequency: 0,
      sqr3DutyCycle: 0,
      sqr3Phase: 0,
      sqr4Frequency: 0,
      sqr4DutyCycle: 0,
      sqr4Phase: 0,
      waveFormS1: 'sine',
      waveFormS2: 'sine',
      mode: 'square',
    };
  }

  componentDidMount() {
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('WAV_GEN_CONFIG', (event, args) => {
      const {
        s1Frequency,
        s2Frequency,
        s2Phase,
        waveFormS1,
        waveFormS2,
        sqr1Frequency,
        sqr1DutyCycle,
        sqr2Frequency,
        sqr2DutyCycle,
        sqr2Phase,
        sqr3Frequency,
        sqr3DutyCycle,
        sqr3Phase,
        sqr4Frequency,
        sqr4DutyCycle,
        sqr4Phase,
        mode,
      } = args;
      this.setState({
        s1Frequency,
        s2Frequency,
        s2Phase,
        waveFormS1,
        waveFormS2,
        sqr1Frequency,
        sqr1DutyCycle,
        sqr2Frequency,
        sqr2DutyCycle,
        sqr2Phase,
        sqr3Frequency,
        sqr3DutyCycle,
        sqr3Phase,
        sqr4Frequency,
        sqr4DutyCycle,
        sqr4Phase,
        mode,
      });
    });
    this.getConfigFromDevice();
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('WAV_GEN_CONFIG');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_WAV_GEN',
      });
  }, 500);

  sendConfigToDevice = debounce(() => {
    const { isConnected } = this.props;
    const {
      s1Frequency,
      s2Frequency,
      s2Phase,
      waveFormS1,
      waveFormS2,
      sqr1Frequency,
      sqr1DutyCycle,
      sqr2Frequency,
      sqr2DutyCycle,
      sqr2Phase,
      sqr3Frequency,
      sqr3DutyCycle,
      sqr3Phase,
      sqr4Frequency,
      sqr4DutyCycle,
      sqr4Phase,
      mode,
    } = this.state;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_WAV_GEN',
        s1Frequency,
        s2Frequency,
        s2Phase,
        waveFormS1,
        waveFormS2,
        sqr1Frequency,
        sqr1DutyCycle,
        sqr2Frequency,
        sqr2DutyCycle,
        sqr2Phase,
        sqr3Frequency,
        sqr3DutyCycle,
        sqr3Phase,
        sqr4Frequency,
        sqr4DutyCycle,
        sqr4Phase,
        mode,
      });
  }, 500);

  onTogglePreview = pinName => event => {
    this.setState(prevState => ({
      activePreview: {
        ...prevState.activePreview,
        [pinName]: !prevState.activePreview[pinName],
      },
    }));
  };

  onChangeWaveForm = pinName => event => {
    this.setState(
      prevState => ({
        [pinName]: event.target.value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onChangeMode = event => {
    this.setState(
      prevState => ({
        mode: event.target.value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  onChangeSlider = parameterType => (event, value) => {
    this.setState(
      prevState => ({
        [parameterType]: value,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
  };

  render() {
    const {
      activePreview,
      s1Frequency,
      s2Frequency,
      s2Phase,
      sqr1Frequency,
      sqr1DutyCycle,
      sqr2Frequency,
      sqr2DutyCycle,
      sqr2Phase,
      sqr3Frequency,
      sqr3DutyCycle,
      sqr3Phase,
      sqr4Frequency,
      sqr4DutyCycle,
      sqr4Phase,
      waveFormS1,
      waveFormS2,
      mode,
    } = this.state;
    return (
      <GraphPanelLayout
        settings={
          <Settings
            activePreview={activePreview}
            s1Frequency={s1Frequency}
            s2Frequency={s2Frequency}
            s2Phase={s2Phase}
            sqr1Frequency={sqr1Frequency}
            sqr1DutyCycle={sqr1DutyCycle}
            sqr2Frequency={sqr2Frequency}
            sqr2DutyCycle={sqr2DutyCycle}
            sqr2Phase={sqr2Phase}
            sqr3Frequency={sqr3Frequency}
            sqr3DutyCycle={sqr3DutyCycle}
            sqr3Phase={sqr3Phase}
            sqr4Frequency={sqr4Frequency}
            sqr4DutyCycle={sqr4DutyCycle}
            sqr4Phase={sqr4Phase}
            waveFormS1={waveFormS1}
            waveFormS2={waveFormS2}
            mode={mode}
            onTogglePreview={this.onTogglePreview}
            onChangeWaveForm={this.onChangeWaveForm}
            onChangeMode={this.onChangeMode}
            onChangeSlider={this.onChangeSlider}
          />
        }
        graph={<Graph activePreview={activePreview} />}
      />
    );
  }
}

export default WaveGenerator;
