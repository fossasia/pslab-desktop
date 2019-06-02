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
} from 'recharts';
import { withTheme } from 'styled-components';

const electron = window.require('electron');
const { ipcRenderer } = electron;

class Graph extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fftData: [
        {
          ch1: 0,
          ch2: 0,
          ch3: 0,
          ch4: 0,
          frequency: 0,
        },
      ],
    };
  }

  componentDidMount() {
    ipcRenderer.on('TO_RENDERER_DATA', (event, args) => {
      this.setState({
        fftData: args.data,
      });
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('TO_RENDERER_DATA');
  }

  render() {
    const { activeChannels, theme } = this.props;
    const { fftData } = this.state;

    return (
      <ResponsiveContainer>
        <LineChart
          data={fftData}
          margin={{
            top: 48,
            right: 0,
            left: 0,
            bottom: 32,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="frequency" type="number" tickCount={11} />
          <YAxis yAxisId="left" allowDataOverflow={true} />
          <YAxis yAxisId="right" orientation="right" allowDataOverflow={true} />
          <Tooltip />
          <Legend align="right" iconType="triangle" />
          {activeChannels.ch1 && (
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="ch1"
              stroke={theme.ch1Color}
              dot={false}
              activeDot={{ r: 4 }}
            />
          )}
          {activeChannels.ch2 && (
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="ch2"
              stroke={theme.ch2Color}
              dot={false}
              activeDot={{ r: 4 }}
            />
          )}
          {activeChannels.ch3 && (
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="ch3"
              stroke={theme.ch3Color}
              dot={false}
              activeDot={{ r: 4 }}
            />
          )}
          {activeChannels.mic && (
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="mic"
              stroke={theme.micColor}
              dot={false}
              activeDot={{ r: 4 }}
            />
          )}
        </LineChart>
      </ResponsiveContainer>
    );
  }
}

export default withTheme(Graph);
