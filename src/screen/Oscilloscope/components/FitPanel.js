import React, { Component } from 'react';
import { Card, Typography, Divider } from '@material-ui/core';
import {
  PanelContainer,
  ValueWrapper,
  DisplayContainer,
} from './FitPanel.styles';
import Display from '../../../components/Display';
import roundOff from '../../../utils/arithmetics';

const electron = window.require('electron');
const { ipcRenderer } = electron;

class FitPanel extends Component {
  constructor(props) {
    super(props);
    this.state = {
      channel1: {
        amplitude: '-/--',
        frequency: '-/--',
        offset: '-/--',
        phase: '-/--',
        dutyCycle: '-/--',
      },
      channel2: {
        amplitude: '-/--',
        frequency: '-/--',
        offset: '-/--',
        phase: '-/--',
        dutyCycle: '-/--',
      },
    };
  }

  componentDidMount = () => {
    ipcRenderer.on('OSC_FIT_DATA', (event, args) => {
      const { isReading, fitType } = this.props;
      const {
        fitOutput1Sine,
        fitOutput2Sine,
        fitOutput1Square,
        fitOutput2Square,
      } = args;
      if (isReading) {
        if (fitType === 'Sine') {
          this.setState({
            channel1: fitOutput1Sine
              ? {
                  amplitude: roundOff(fitOutput1Sine[0], 3),
                  frequency: roundOff(fitOutput1Sine[1], 3),
                  offset: roundOff(fitOutput1Sine[2], 3),
                  phase: roundOff(fitOutput1Sine[3], 3),
                }
              : {
                  amplitude: '--/-',
                  frequency: '--/-',
                  offset: '--/-',
                  phase: '--/-',
                },
            channel2: fitOutput2Sine
              ? {
                  amplitude: roundOff(fitOutput2Sine[0], 3),
                  frequency: roundOff(fitOutput2Sine[1], 3),
                  offset: roundOff(fitOutput2Sine[2], 3),
                  phase: roundOff(fitOutput2Sine[3], 3),
                }
              : {
                  amplitude: '--/-',
                  frequency: '--/-',
                  offset: '--/-',
                  phase: '--/-',
                },
          });
        } else {
          this.setState({
            channel1: fitOutput1Square
              ? {
                  amplitude: roundOff(fitOutput1Square[0], 3),
                  frequency: roundOff(fitOutput1Square[1], 3),
                  phase: roundOff(fitOutput1Square[2], 3),
                  dutyCycle: roundOff(fitOutput1Square[3], 3),
                  offset: roundOff(fitOutput1Square[4], 3),
                }
              : {
                  amplitude: '--/-',
                  frequency: '--/-',
                  offset: '--/-',
                  phase: '--/-',
                  dutyCycle: '--/-',
                },
            channel2: fitOutput2Square
              ? {
                  amplitude: roundOff(fitOutput2Square[0], 3),
                  frequency: roundOff(fitOutput2Square[1], 3),
                  phase: roundOff(fitOutput2Square[2], 3),
                  dutyCycle: roundOff(fitOutput1Square[3], 3),
                  offset: roundOff(fitOutput2Square[4], 3),
                }
              : {
                  amplitude: '--/-',
                  frequency: '--/-',
                  offset: '--/-',
                  phase: '--/-',
                  dutyCycle: '--/-',
                },
          });
        }
      }
    });
  };

  componentWillUnmount = () => {
    ipcRenderer.removeAllListeners('OSC_FIT_DATA');
  };

  render() {
    const { fitType, fitChannel1, fitChannel2 } = this.props;
    const { channel1, channel2 } = this.state;
    return (
      <PanelContainer>
        {fitChannel1 !== 'None' && (
          <Card>
            <Typography
              style={{ padding: '0.6rem' }}
              component="h6"
              variant="h6"
            >
              {fitChannel1}
            </Typography>
            <Divider />
            {fitType === 'Sine' && (
              <DisplayContainer>
                <ValueWrapper>
                  <div>Amplitude</div>
                  <Display fontSize={1} value={channel1.amplitude} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Frequency</div>
                  <Display fontSize={1} value={channel1.frequency} unit="Hz" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Offset</div>
                  <Display fontSize={1} value={channel1.offset} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Phase</div>
                  <Display fontSize={1} value={channel1.phase} unit="Deg" />
                </ValueWrapper>
              </DisplayContainer>
            )}
            {fitType === 'Square' && (
              <DisplayContainer>
                <ValueWrapper>
                  <div>Amplitude</div>
                  <Display fontSize={1} value={channel1.amplitude} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Frequency</div>
                  <Display fontSize={1} value={channel1.frequency} unit="Hz" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Offset</div>
                  <Display fontSize={1} value={channel1.offset} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Phase</div>
                  <Display fontSize={1} value={channel1.phase} unit="Deg" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Duty Cycle</div>
                  <Display fontSize={1} value={channel1.dutyCycle} unit="%" />
                </ValueWrapper>
              </DisplayContainer>
            )}
          </Card>
        )}
        {fitChannel2 !== 'None' && (
          <Card>
            <Typography
              style={{ padding: '0.6rem' }}
              component="h6"
              variant="h6"
            >
              {fitChannel2}
            </Typography>
            <Divider />
            {fitType === 'Sine' && (
              <DisplayContainer>
                <ValueWrapper>
                  <div>Amplitude</div>
                  <Display fontSize={1} value={channel2.amplitude} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Frequency</div>
                  <Display fontSize={1} value={channel2.frequency} unit="Hz" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Offset</div>
                  <Display fontSize={1} value={channel2.offset} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Phase</div>
                  <Display fontSize={1} value={channel2.phase} unit="Deg" />
                </ValueWrapper>
              </DisplayContainer>
            )}
            {fitType === 'Square' && (
              <DisplayContainer>
                <ValueWrapper>
                  <div>Amplitude</div>
                  <Display fontSize={1} value={channel2.amplitude} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Frequency</div>
                  <Display fontSize={1} value={channel2.frequency} unit="Hz" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Offset</div>
                  <Display fontSize={1} value={channel2.offset} unit="V" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Phase</div>
                  <Display fontSize={1} value={channel2.phase} unit="Deg" />
                </ValueWrapper>
                <ValueWrapper>
                  <div>Duty Cycle</div>
                  <Display fontSize={1} value={channel2.dutyCycle} unit="%" />
                </ValueWrapper>
              </DisplayContainer>
            )}
          </Card>
        )}
      </PanelContainer>
    );
  }
}

export default FitPanel;
