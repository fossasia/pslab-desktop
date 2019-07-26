import React, { Component } from 'react';
import { connect } from 'react-redux';
import debounce from 'lodash/debounce';
import { Container, Wrapper } from './styles';
import AnalogController from './components/AnalogController';
import DigitalController from './components/DigitalController';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class WaveGenerator extends Component {
  constructor(props) {
    super(props);
    this.state = {
      wave: false,
      digital: true,
      s1Frequency: 10,
      s2Frequency: 10,
      s2Phase: 0,
      pwmFrequency: 0,
      sqr1DutyCycle: 0,
      sqr2DutyCycle: 0,
      sqr2Phase: 0,
      sqr3DutyCycle: 0,
      sqr3Phase: 0,
      sqr4DutyCycle: 0,
      sqr4Phase: 0,
      waveFormS1: 'sine',
      waveFormS2: 'sine',
    };
  }

  componentDidMount() {
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    ipcRenderer.on('WAV_GEN_CONFIG', (event, args) => {
      const {
        wave,
        digital,
        s1Frequency,
        s2Frequency,
        s2Phase,
        waveFormS1,
        waveFormS2,
        pwmFrequency,
        sqr1DutyCycle,
        sqr2DutyCycle,
        sqr2Phase,
        sqr3DutyCycle,
        sqr3Phase,
        sqr4DutyCycle,
        sqr4Phase,
      } = args;
      this.setState({
        wave,
        digital,
        s1Frequency,
        s2Frequency,
        s2Phase,
        waveFormS1,
        waveFormS2,
        pwmFrequency,
        sqr1DutyCycle,
        sqr2DutyCycle,
        sqr2Phase,
        sqr3DutyCycle,
        sqr3Phase,
        sqr4DutyCycle,
        sqr4Phase,
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
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SET_CONFIG_WAV_GEN',
        ...this.state,
      });
  }, 500);

  onTogglePreview = event => {
    this.setState(
      prevState => ({
        wave: !prevState.wave,
        digital: !prevState.digital,
      }),
      () => {
        this.sendConfigToDevice();
      },
    );
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
      wave,
      digital,
      s1Frequency,
      s2Frequency,
      s2Phase,
      pwmFrequency,
      sqr1DutyCycle,
      sqr2DutyCycle,
      sqr2Phase,
      sqr3DutyCycle,
      sqr3Phase,
      sqr4DutyCycle,
      sqr4Phase,
      waveFormS1,
      waveFormS2,
    } = this.state;
    return (
      <Container>
        <Wrapper>
          {wave ? (
            <AnalogController
              s1Frequency={s1Frequency}
              s2Frequency={s2Frequency}
              s2Phase={s2Phase}
              waveFormS1={waveFormS1}
              waveFormS2={waveFormS2}
              onChangeWaveForm={this.onChangeWaveForm}
              onChangeSlider={this.onChangeSlider}
              onTogglePreview={this.onTogglePreview}
            />
          ) : (
            <DigitalController
              pwmFrequency={pwmFrequency}
              sqr1DutyCycle={sqr1DutyCycle}
              sqr2DutyCycle={sqr2DutyCycle}
              sqr2Phase={sqr2Phase}
              sqr3DutyCycle={sqr3DutyCycle}
              sqr3Phase={sqr3Phase}
              sqr4DutyCycle={sqr4DutyCycle}
              sqr4Phase={sqr4Phase}
              onChangeSlider={this.onChangeSlider}
              onTogglePreview={this.onTogglePreview}
            />
          )}
        </Wrapper>
      </Container>
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default connect(
  mapStateToProps,
  null,
)(WaveGenerator);
