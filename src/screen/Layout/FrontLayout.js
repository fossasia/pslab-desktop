import React from 'react';
import Tooltip from '@material-ui/core/Tooltip';
import FrontLayoutImg from '../../resources/front_layout.png';
import { ImageContainer, Marker } from './styles';

const FrontLayout = () => {
  return (
    <div
      style={{
        height: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <ImageContainer>
        {/* I2C */}
        <img src={FrontLayoutImg} alt=""></img>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={430}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Voltage supply pin ( 3.3 V )
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={457}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Serial clock pin for I2C</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={485}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Serial data pin for I2C</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={515}></Marker>
        </Tooltip>
        {/* I2C */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={575}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Voltage supply pin ( 3.3 V )
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={601}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Serial clock pin for I2C</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={627}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Serial data pin for I2C</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={655}></Marker>
        </Tooltip>
        {/* Power Source */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={710}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Programmable current source (3.3 mA)
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={735}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={763}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Programmable voltage source 3 (0 - 3.3 V)
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={792}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={822}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Programmable voltage source 2 (±3.3 V)
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={847}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={877}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Programmable voltage source 1 (-+5 V)
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={32} left={905}></Marker>
        </Tooltip>
        {/* BlueTooth Source */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Bluetooth device enable/disable pin
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={190} left={385}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Voltage supply pin (+5V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={222} left={385}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={252} left={385}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Transmitter pin for UART communication
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={280} left={385}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Receiver pin for UART communication
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={308} left={385}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Bluetooth device state output pin
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={336} left={385}></Marker>
        </Tooltip>
        {/* ICSP Source */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Master clear pin for programmer
              </div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={382} left={285}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Voltage supply pin (3.3 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={382} left={313}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={382} left={338}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Data pin for programmer</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={382} left={365}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Clock pin for programmer</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={382} left={393}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Mode pin for programmer</div>
            </React.Fragment>
          }
          placement="top"
        >
          <Marker top={382} left={421}></Marker>
        </Tooltip>
        {/* UART */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={315}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>ESP programmer pin</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={343}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Receiver pin for UART communication
              </div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={371}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Transmitter pin for UART communication
              </div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={398}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={425}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Voltage supply pin (5 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={457}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Voltage supply pin (3.3 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={487}></Marker>
        </Tooltip>
        {/* Wave generator */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={542}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Wave generator pin 1</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={572}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={600}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Wave generator pin 2</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={629}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={658}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>PWM generator pin 1</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={687}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={714}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>PWM generator pin 2</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={742}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={771}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>PWM generator pin 3</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={799}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={825}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>PWM generator pin 4</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={853}></Marker>
        </Tooltip>
        {/* Logic Analyser */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 1</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={907}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 2</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={935}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 3</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={964}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 4</div>
            </React.Fragment>
          }
          placement="bottom"
        >
          <Marker top={568} left={990}></Marker>
        </Tooltip>
        {/* Oscilloscope */}
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Voltage measurement pin</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={122} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={122} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Resistance measurement pin</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={147} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={147} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Capacitance measurement pin
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={175} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={175} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Frequency counter pin</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={205} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={205} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>External microphone input</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={235} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={235} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Oscilloscope channel 3 gain set
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={264} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={264} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Oscilloscope channel 3 input
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={293} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={293} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Oscilloscope channel 2 input
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={319} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={319} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>
                Oscilloscope channel 1 input
              </div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={347} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={347} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Alternative channel input</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={376} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={376} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 4</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={403} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={403} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 3</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={432} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={432} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 2</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={458} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={458} left={1075}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Logic analyzer pin 1</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={485} left={1047}></Marker>
        </Tooltip>
        <Tooltip
          title={
            <React.Fragment>
              <div style={{ fontSize: '16px' }}>Ground pin (0 V)</div>
            </React.Fragment>
          }
          placement="right"
        >
          <Marker top={485} left={1075}></Marker>
        </Tooltip>
      </ImageContainer>
    </div>
  );
};

export default FrontLayout;
