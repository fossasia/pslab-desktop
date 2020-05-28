import React from 'react';
import { connect } from 'react-redux';
import { Container, Wrapper, Steps, Link, Hr } from './DeviceScreen.styles';
import DisconnectedImage from '../../resources/ds_discon.png';
import ConnectedImage from '../../resources/ds_con.png';

const DeviceScreen = ({ isConnected, deviceInformation }) => {
  return isConnected ? (
    <Container>
      <Wrapper>
        <img
          alt=""
          src={ConnectedImage}
          style={{
            height: '104px',
            width: '104px',
            margin: '16px 16px 16px 16px',
          }}
        />
        <div
          style={{
            margin: '0px 0px 32px 0px',
            fontSize: '18px',
            color: 'gray',
          }}
        >
          <b>Device Connected Successfully</b>
        </div>
        <div
          style={{
            margin: '0px 0px 32px 0px',
            fontSize: '18px',
            color: 'gray',
          }}
        >
          <b>{deviceInformation.deviceName}</b>
        </div>
        <Hr></Hr>
        <Link
          onClick={() => {
            window.open(
              'https://pslab.io/',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <u>What is PSLab Device?</u>
        </Link>
      </Wrapper>
    </Container>
  ) : (
    <Container>
      <Wrapper>
        <img
          alt=""
          src={DisconnectedImage}
          style={{
            height: '104px',
            width: '104px',
            margin: '16px 16px 16px 16px',
          }}
        />
        <div
          style={{
            margin: '0px 0px 32px 0px',
            fontSize: '18px',
            color: 'gray',
          }}
        >
          <b>No USB Device Found</b>
        </div>
        <div
          style={{
            margin: '0px 0px 16px 0px',
            fontSize: '18px',
          }}
        >
          <u>
            <b>Steps to connect the PSLab Device</b>
          </u>
        </div>
        <Steps>
          <div
            style={{
              margin: '0px 0px 8px 0px',
            }}
          >
            1. Connect the other end of the micro USB cable to a USB adapter
          </div>
          <div
            style={{
              margin: '0px 0px 8px 0px',
            }}
          >
            2. Connect the adapter to your PC
          </div>
          <div
            style={{
              margin: '0px 0px 8px 0px',
            }}
          >
            3. Start the Desktop app
          </div>
        </Steps>
        <Hr></Hr>
        <Link
          onClick={() => {
            window.open(
              'https://pslab.io/',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <u>What is PSLab Device?</u>
        </Link>
      </Wrapper>
    </Container>
  );
};

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
  deviceInformation: state.app.device.deviceInformation,
});

export default connect(mapStateToProps, null)(DeviceScreen);
