import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import debounce from 'lodash/debounce';
import Button from '@material-ui/core/Button';
import {
  Container,
  Wrapper,
  HelpText,
  SecondaryContentWrapper,
  TitleWrapper,
  ScrollWrapper,
  SensorTab,
  SensorTitle,
} from './styles';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

// see PSL/sensorlist.py for the mapping
const knownSensors = [
  {
    id: 0x48, // TODO: check duplicate definitions
    name: 'ADS1115',
  },
  {
    id: 0x77,
    name: 'BMP180',
  },
  {
    id: 0x5a,
    name: 'MLX90614',
  },
  {
    id: 0x1e,
    name: 'HMC5883L',
  },
  {
    id: 0x68,
    name: 'MPU6050',
  },
  {
    id: 0x29,
    name: 'VL53LXX', // TODO: implement in Python lib
    description: 'Time-of-flight',
  },
  {
    id: 0x40,
    name: 'SHT21',
    description: 'Temperature and humidity',
  },
  {
    id: 0x49,
    name: 'TSL2561',
  },
];

const filterKnownSensors = (detectedSensors = []) => {
  // PSL always lists 0 and 96, regardless of whether a sensor is present
  const filtered = detectedSensors.filter(s => s !== 96 && s !== 0);
  return knownSensors.filter(k => filtered.includes(k.id));
};

const SensorList = ({ sensors = [], onReadSensor = () => {} }) => (
  <ScrollWrapper>
    {sensors.map((item, index) => {
      return (
        <SensorTab key={index} onClick={() => onReadSensor(item)}>
          <SensorTitle>
            {item.name} {item.description}
          </SensorTitle>
        </SensorTab>
      );
    })}
  </ScrollWrapper>
);

// TODO: implement reading from sensor

class Sensors extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isScanned: false,
      sensorList: [],
      data: null,
      sensorData: null,
    };
  }

  componentDidMount() {
    // TODO: Other components are implemented this way. Check how it applies
    // here.
    /*
    ipcRenderer.on('CONNECTION_STATUS', (event, args) => {
      const { isConnected } = args;
      isConnected && this.getConfigFromDevice();
    });
    */
    ipcRenderer.on('SENSORS_SCAN', (event, args) => {
      this.setState({
        data: args.data,
        isScanned: true,
        sensorList: filterKnownSensors(args.data),
      });
    });
    ipcRenderer.on('SENSORS_READ', (event, args) => {
      this.setState({
        isScanned: true,
        sensorData: args.data,
      });
    });
    // this.getConfigFromDevice();
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('SENSORS_SCAN');
    ipcRenderer.removeAllListeners('SENSORS_READ');
  }

  getConfigFromDevice = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'GET_CONFIG_SENSORS',
      });
  }, 500);

  scan = debounce(() => {
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SENSORS_SCAN',
      });
  }, 500);

  onReadSensor = debounce(sensor => {
    // TODO: use sensor and implement switch over it
    // TODO: can we find a generic interface?
    console.info({ sensor });
    const { isConnected } = this.props;
    isConnected &&
      loadBalancer.sendData(ipcRenderer, 'linker', {
        command: 'SENSORS_READ',
      });
  }, 500);

  render() {
    const { data, isScanned, sensorList, sensorData } = this.state;

    return (
      <Container>
        <SecondaryContentWrapper>
          <Button variant="contained" color="secondary" onClick={this.scan}>
            AUTOSCAN
          </Button>
          <HelpText>
            {!isScanned && sensorList.length === 0
              ? 'Use Autoscan button to find connected sensors to PSLab device'
              : 'Scan complete'}
          </HelpText>
        </SecondaryContentWrapper>
        <Wrapper>
          {isScanned &&
            (sensorList.length > 0 ? (
              <>
                <TitleWrapper>Detected sensors</TitleWrapper>
                <SensorList
                  sensors={sensorList}
                  onReadSensor={this.onReadSensor}
                />
              </>
            ) : (
              <TitleWrapper>No sensors detected</TitleWrapper>
            ))}
          Sensor data: <pre>{JSON.stringify(sensorData)}</pre>
          <TitleWrapper>Known sensors</TitleWrapper>
          <SensorList sensors={knownSensors} />
          <pre>{JSON.stringify(data)}</pre>
        </Wrapper>
      </Container>
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default withRouter(connect(mapStateToProps, null)(Sensors));
