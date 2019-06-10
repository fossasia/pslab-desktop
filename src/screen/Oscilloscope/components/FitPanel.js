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
      },
      channel2: {
        amplitude: '-/--',
        frequency: '-/--',
        offset: '-/--',
        phase: '-/--',
      },
    };
  }

  componentDidMount = () => {
    ipcRenderer.on('OSC_FIT_DATA', (event, args) => {
      const { isReading } = this.props;
      const { fitOutput1, fitOutput2 } = args;
      isReading &&
        this.setState({
          channel1:
            fitOutput1 !== null && fitOutput1 !== false
              ? {
                  amplitude: roundOff(fitOutput1[0], 3),
                  frequency: roundOff(fitOutput1[1], 3),
                  offset: roundOff(fitOutput1[2], 3),
                  phase: roundOff(fitOutput1[3], 3),
                }
              : {
                  amplitude: '--/-',
                  frequency: '--/-',
                  offset: '--/-',
                  phase: '--/-',
                },
          channel2:
            fitOutput2 !== null && fitOutput2 !== false
              ? {
                  amplitude: roundOff(fitOutput2[0], 3),
                  frequency: roundOff(fitOutput2[1], 3),
                  offset: roundOff(fitOutput2[2], 3),
                  phase: roundOff(fitOutput2[3], 3),
                }
              : {
                  amplitude: '--/-',
                  frequency: '--/-',
                  offset: '--/-',
                  phase: '--/-',
                },
        });
    });
  };

  componentWillUnmount = () => {
    ipcRenderer.removeAllListeners('OSC_FIT_DATA');
  };

  render() {
    const { fitChannel1, fitChannel2 } = this.props;
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
          </Card>
        )}
      </PanelContainer>
    );
  }
}

export default FitPanel;
