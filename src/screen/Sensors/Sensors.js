import React, { Component } from 'react';
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

class Sensors extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isScanned: false,
      sensorList: [],
    };
    this.defaultSensorList = [
      {
        name: 'ADS1115',
      },
      {
        name: 'BMP180',
      },
      {
        name: 'MLX90614',
      },
      {
        name: 'HMC5883L',
      },
      {
        name: 'MPU6050',
      },
      {
        name: 'SHT21',
      },
      {
        name: 'TSL2561',
      },
    ];
  }

  render() {
    const { isScanned, sensorList } = this.state;

    return (
      <Container>
        <Wrapper>
          <SecondaryContentWrapper>
            <Button variant="contained" color="secondary">
              AUTOSCAN
            </Button>
            <HelpText>
              {!isScanned && sensorList.length === 0
                ? 'Use Autoscan button to find connected sensors to PSLab device'
                : 'Not Connected'}
            </HelpText>
          </SecondaryContentWrapper>
          {isScanned && <TitleWrapper>SELECT SENSOR</TitleWrapper>}
          {isScanned && sensorList.length === 0 && (
            <ScrollWrapper>
              {this.defaultSensorList.map((item, index) => {
                return (
                  <SensorTab key={index}>
                    <SensorTitle>{item.name}</SensorTitle>
                  </SensorTab>
                );
              })}
            </ScrollWrapper>
          )}
          {isScanned && sensorList.length !== 0 && (
            <ScrollWrapper>
              {sensorList.map((item, index) => {
                return (
                  <SensorTab key={index}>
                    <SensorTitle>{item.name}</SensorTitle>
                  </SensorTab>
                );
              })}
            </ScrollWrapper>
          )}
        </Wrapper>
      </Container>
    );
  }
}

export default Sensors;
