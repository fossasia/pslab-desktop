import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
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
import { withTheme } from 'styled-components';
const electron = window.require('electron');
const { ipcRenderer } = electron;

const Graph = ({
  isReading,
  activeChannels,
  timeBase,
  channelRanges,
  theme,
}) => {
  const [oscData, setOscData] = useState([
    {
      ch1: 0,
      ch2: 0,
      ch3: 0,
      ch4: 0,
      time: 0,
    },
  ]);

  useEffect(() => {
    ipcRenderer.on('OSC_VOLTAGE_DATA', (event, args) => {
      isReading && setOscData(args.data);
    });
    return () => {
      ipcRenderer.removeAllListeners('OSC_VOLTAGE_DATA');
    };
  }, [isReading]);

  return (
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
        <XAxis
          dataKey="time"
          type="number"
          tickCount={11}
          domain={[0, 10 * timeBase]}
        >
          <Label value="mSec" position="bottom" />
        </XAxis>
        <YAxis
          yAxisId="left"
          domain={[
            -1 * parseInt(channelRanges.ch1, 10),
            parseInt(channelRanges.ch1, 10),
          ]}
          allowDataOverflow={true}
          label="V"
        />
        <YAxis
          yAxisId="right"
          domain={[
            -1 * parseInt(channelRanges.ch2, 10),
            parseInt(channelRanges.ch2, 10),
          ]}
          orientation="right"
          allowDataOverflow={true}
        />
        {!isReading && <Tooltip />}
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
            yAxisId="right"
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
};

const mapStateToProps = state => {
  const {
    isReading,
    activeChannels,
    timeBase,
    channelRanges,
  } = state.oscilloscope;
  return {
    isReading,
    activeChannels,
    timeBase,
    channelRanges,
  };
};

export default withTheme(
  connect(
    mapStateToProps,
    null,
  )(Graph),
);
