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
import { GraphWrapper, ProgressWrapper } from './Settings.styles';

const electron = window.require('electron');
const { ipcRenderer } = electron;

class Graph extends Component {
  constructor(props) {
    super(props);
    this.state = {
      LA1Data: [
        {
          voltage: 0,
          time: 0,
        },
      ],
      LA2Data: [
        {
          voltage: 0,
          time: 0,
        },
      ],
      LA3Data: [
        {
          voltage: 0,
          time: 0,
        },
      ],
      LA4Data: [
        {
          voltage: 0,
          time: 0,
        },
      ],
    };
  }

  componentDidMount() {
    ipcRenderer.on('LA_DATA', (event, args) => {
      const { isReading, toggleRead } = this.props;
      if (isReading) {
        this.setState({
          ...args.data,
        });
        toggleRead();
      }
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('LA_DATA');
  }

  render() {
    const { numberOfChannels, isReading, theme } = this.props;
    const { LA1Data, LA2Data, LA3Data, LA4Data } = this.state;

    return (
      <GraphWrapper>
        <ProgressWrapper>{isReading && <LinearProgress />}</ProgressWrapper>
        <ResponsiveContainer>
          <LineChart
            margin={{
              top: 48,
              right: 0,
              left: 0,
              bottom: 32,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="time"
              type="number"
              domain={[0, dataMax => Math.round(dataMax)]}
              allowDecimals={false}
              tickCount={20}
              interval="preserveStart"
            >
              <Label value="mSec" position="bottom" />
            </XAxis>
            <YAxis yAxisId="left" domain={['dataMin - 2', 'dataMax + 2']} />
            <YAxis dataKey="voltage" yAxisId="right" orientation="right" />
            <Tooltip />
            <Legend align="right" iconType="triangle" />
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="voltage"
              data={LA1Data}
              stroke={theme.ch1Color}
              dot={false}
              activeDot={{ r: 4 }}
              name="LA1"
            />
            {numberOfChannels > 1 && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="voltage"
                data={LA2Data}
                stroke={theme.ch2Color}
                dot={false}
                activeDot={{ r: 4 }}
                name="LA2"
              />
            )}
            {numberOfChannels > 2 && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="voltage"
                data={LA3Data}
                stroke={theme.ch3Color}
                dot={false}
                activeDot={{ r: 4 }}
                name="LA3"
              />
            )}
            {numberOfChannels > 3 && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="voltage"
                data={LA4Data}
                stroke={theme.micColor}
                dot={false}
                activeDot={{ r: 4 }}
                name="LA4"
              />
            )}
          </LineChart>
        </ResponsiveContainer>
      </GraphWrapper>
    );
  }
}

export default withTheme(Graph);
