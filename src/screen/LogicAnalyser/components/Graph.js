import React, { Component } from 'react';
import {
  ResponsiveContainer,
  Line,
  LineChart,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  Label,
} from 'recharts';
import { LinearProgress } from '@material-ui/core';
import { withTheme } from 'styled-components';
import { GraphWrapper,ProgressWrapper } from './Settings.styles';

const electron = window.require('electron');
const { ipcRenderer } = electron;

class Graph extends Component {
  constructor(props) {
    super(props);
    this.state = {
      oscData: [
        {
          ch1: 0,
          ch2: 0,
          ch3: 0,
          ch4: 0,
          time: 0,
        },
      ],
    };
  }

  componentDidMount() {
    ipcRenderer.on('OSC_VOLTAGE_DATA', (event, args) => {
      const { isReading } = this.props;
      isReading &&
        this.setState({
          oscData: args.data,
        });
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('OSC_VOLTAGE_DATA');
  }

  render() {
    const { numberOfChannels, isReading, theme } = this.props;
    const { oscData } = this.state;

    return (
      <GraphWrapper>
        <ProgressWrapper>{isReading && <LinearProgress />}</ProgressWrapper>
        <ResponsiveContainer>
          <LineChart
            data={oscData}
            margin={{
              top: 48,
              right: 0,
              left: 0,
              bottom: 32,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" type="number">
              <Label value="mSec" position="bottom" />
            </XAxis>
            <YAxis yAxisId="left" />
            <YAxis yAxisId="right" orientation="right" />
            <Tooltip />
            <Legend align="right" iconType="triangle" />
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="ch1"
              stroke={theme.ch1Color}
              dot={false}
              activeDot={{ r: 4 }}
            />
            {numberOfChannels > 1 && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="ch2"
                stroke={theme.ch2Color}
                dot={false}
                activeDot={{ r: 4 }}
              />
            )}
            {numberOfChannels > 2 && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="ch3"
                stroke={theme.ch3Color}
                dot={false}
                activeDot={{ r: 4 }}
              />
            )}
            {numberOfChannels > 3 && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="ch4"
                stroke={theme.micColor}
                dot={false}
                activeDot={{ r: 4 }}
              />
            )}
          </LineChart>
        </ResponsiveContainer>
      </GraphWrapper>
    );
  }
}

export default withTheme(Graph);
