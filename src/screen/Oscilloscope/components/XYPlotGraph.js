import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import {
  ResponsiveContainer,
  Line,
  LineChart,
  XAxis,
  YAxis,
  CartesianGrid,
  Label,
} from 'recharts';
import { withTheme } from 'styled-components';
const electron = window.require('electron');
const { ipcRenderer } = electron;

const XYPlotGraph = ({ isReading, plotChannel1, plotChannel2, theme }) => {
  const [xyPlotData, setXyPlotData] = useState([
    {
      plotChannel1: 0,
      plotChannel2: 0,
    },
  ]);

  useEffect(() => {
    ipcRenderer.on('OSC_XY_PLOT_DATA', (event, args) => {
      console.log(args);
      isReading && setXyPlotData(args.data);
    });
    return () => {
      ipcRenderer.removeAllListeners('OSC_XY_PLOT_DATA');
    };
  }, [isReading]);

  return (
    <ResponsiveContainer>
      <LineChart
        data={xyPlotData}
        margin={{
          top: 48,
          right: 0,
          left: 0,
          bottom: 32,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="plotChannel1"
          type="number"
          allowDecimals={false}
          interval="preserveStartEnd"
        >
          <Label value={plotChannel1} position="bottom" />
        </XAxis>
        <YAxis
          yAxisId="left"
          allowDecimals={false}
          interval="preserveStartEnd"
          label={plotChannel2}
        />
        <YAxis yAxisId="right" orientation="right" />
        <Line
          yAxisId="left"
          type="monotone"
          dataKey="plotChannel2"
          stroke={theme.ch1Color}
          dot={false}
          activeDot={{ r: 4 }}
        />
      </LineChart>
    </ResponsiveContainer>
  );
};

const mapStateToProps = state => {
  const { isReading, plotChannel1, plotChannel2 } = state.oscilloscope;
  return {
    isReading,
    plotChannel1,
    plotChannel2,
  };
};

export default withTheme(
  connect(
    mapStateToProps,
    null,
  )(XYPlotGraph),
);
