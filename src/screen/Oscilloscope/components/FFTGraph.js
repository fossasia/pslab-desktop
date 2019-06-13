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

const Graph = ({ isReading, activeChannels, theme }) => {
  const [fftData, setFftData] = useState([
    {
      ch1: 0,
      ch2: 0,
      ch3: 0,
      ch4: 0,
      frequency: 0,
    },
  ]);

  useEffect(() => {
    ipcRenderer.on('OSC_FFT_DATA', (event, args) => {
      isReading && setFftData(args.data);
    });
    return () => {
      ipcRenderer.removeAllListeners('OSC_FFT_DATA');
    };
  }, [isReading]);

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
        <XAxis dataKey="frequency" type="number" tickCount={11}>
          <Label value="Hz" position="bottom" />
        </XAxis>
        <YAxis yAxisId="left" allowDataOverflow={true} label="V" />
        <YAxis yAxisId="right" orientation="right" allowDataOverflow={true} />
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
};

const mapStateToProps = state => {
  const { isReading, activeChannels } = state.oscilloscope;
  return {
    isReading,
    activeChannels,
  };
};

export default withTheme(
  connect(
    mapStateToProps,
    null,
  )(Graph),
);
