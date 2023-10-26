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
const loadBalancer = window.require('electron-load-balancer');

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
      const { isReading, toggleRead, isAutoReading } = this.props;
      if (isReading) {
        this.setState({
          ...args.data,
        });
        toggleRead();
        const reducer = (accumulator, currentArray) =>
          accumulator && currentArray.length == 0;
        const noEventsDetected = Object.values(args.data).reduce(reducer, true);
        if (isAutoReading && noEventsDetected) {
          toggleRead();
        }
      }
    });

    ipcRenderer.on('FETCH_LA', (event, args) => {
      const { LA1Data, LA2Data, LA3Data, LA4Data } = this.state;
      const { dataPath, numberOfChannels } = this.props;
      loadBalancer.sendData(ipcRenderer, 'playback', {
        command: 'WRITE_LA',
        LA1Voltage: LA1Data ? LA1Data.map(item => item.voltage) : [],
        LA1Time: LA1Data ? LA1Data.map(item => item.time) : [],
        LA2Voltage: LA2Data ? LA2Data.map(item => item.voltage) : [],
        LA2Time: LA2Data ? LA2Data.map(item => item.time) : [],
        LA3Voltage: LA3Data ? LA3Data.map(item => item.voltage) : [],
        LA3Time: LA3Data ? LA3Data.map(item => item.time) : [],
        LA4Voltage: LA4Data ? LA4Data.map(item => item.voltage) : [],
        LA4Time: LA4Data ? LA4Data.map(item => item.time) : [],
        numberOfChannels,
        dataPath,
      });
      setTimeout(() => {
        loadBalancer.stop(ipcRenderer, 'playback');
      }, 500);
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('LA_DATA');
    ipcRenderer.removeAllListeners('FETCH_LA');
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
              <Label value="μs" position="bottom" />
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
