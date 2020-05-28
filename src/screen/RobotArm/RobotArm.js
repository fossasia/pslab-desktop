import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Container, KnobWrapper, PaintWrapper } from './RobotArm.styles';
import PaintArea from './Components/PaintArea';
import KnobControl from './Components/KnobControl';
import range from 'lodash/range';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class RobotArm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      brush1: 0,
      brush2: 0,
      brush3: 0,
      brush4: 0,
      servo1: range(60).map(item => null),
      servo2: range(60).map(item => null),
      servo3: range(60).map(item => null),
      servo4: range(60).map(item => null),
      activeBrush: null,
      active: false,
      timeLine: 0,
    };
    this.timer = null;
  }

  componentDidMount() {
    ipcRenderer.on('FETCH_ROB_ARM', (event, args) => {
      const { servo1, servo2, servo3, servo4 } = this.state;
      const { dataPath } = this.props;
      loadBalancer.sendData(ipcRenderer, 'playback', {
        command: 'WRITE_ROB_ARM',
        servo1,
        servo2,
        servo3,
        servo4,
        dataPath,
      });
      setTimeout(() => {
        loadBalancer.stop(ipcRenderer, 'playback');
      }, 500);
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('FETCH_ROB_ARM');
  }

  sendCommand = () => {
    const { active, timeLine, servo1, servo2, servo3, servo4 } = this.state;
    if (timeLine < 60) {
      active &&
        this.setState(
          prevState => ({ timeLine: prevState.timeLine + 1 }),
          () => {
            loadBalancer.sendData(ipcRenderer, 'linker', {
              command: 'SET_ROBO_ARM',
              angle1: servo1[timeLine],
              angle2: servo2[timeLine],
              angle3: servo3[timeLine],
              angle4: servo4[timeLine],
            });
          },
        );
    } else {
      this.stop();
    }
  };

  start = () => {
    this.setState(
      {
        active: true,
      },
      () => {
        if (this.timer === null) {
          this.timer = setInterval(this.sendCommand, 1000);
        }
      },
    );
  };

  pause = () => {
    this.setState({
      active: false,
    });
  };

  stop = () => {
    clearInterval(this.timer);
    this.timer = null;
    this.setState({
      active: false,
      timeLine: 0,
    });
  };

  changeBrushValue = brushNumber => value => {
    this.setState({
      [brushNumber]: value,
    });
  };

  setActiveBrush = value => {
    this.setState({
      activeBrush: value,
    });
  };

  setServoValues = (value, servoType, index) => {
    let newArray = [...this.state[servoType]];
    newArray[index] = value;
    this.setState({
      [servoType]: newArray,
    });
  };

  render() {
    const {
      brush1,
      brush2,
      brush3,
      brush4,
      servo1,
      servo2,
      servo3,
      servo4,
      activeBrush,
      timeLine,
      active,
    } = this.state;

    const { isConnected } = this.props;

    return (
      <Container>
        <KnobWrapper>
          <KnobControl
            isConnected={isConnected}
            changeBrushValue={this.changeBrushValue}
            brush1={brush1}
            brush2={brush2}
            brush3={brush3}
            brush4={brush4}
            setActiveBrush={this.setActiveBrush}
            start={this.start}
            pause={this.pause}
            stop={this.stop}
            active={active}
          />
        </KnobWrapper>
        <PaintWrapper>
          <PaintArea
            timeLine={timeLine}
            brush1={brush1}
            brush2={brush2}
            brush3={brush3}
            brush4={brush4}
            servo1={servo1}
            servo2={servo2}
            servo3={servo3}
            servo4={servo4}
            activeBrush={activeBrush}
            setServoValues={this.setServoValues}
          />
        </PaintWrapper>
      </Container>
    );
  }
}

const mapStateToProps = state => ({
  isConnected: state.app.device.isConnected,
});

export default connect(mapStateToProps, null)(RobotArm);
