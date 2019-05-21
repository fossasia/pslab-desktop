import React from 'react';
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

const Graph = ({
  data,
  isMicActive,
  activeChannels,
  timeBase,
  channelRanges,
  theme,
}) => {
  // console.log(data, isMicActive, activeChannels);

  const yDomain = Math.max(
    parseInt(channelRanges.ch1, 10),
    parseInt(channelRanges.ch2, 10),
  );

  return (
    <ResponsiveContainer>
      <LineChart
        data={data}
        margin={{
          top: 48,
          right: 0,
          left: 0,
          bottom: 32,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="timeGap"
          type="number"
          tickCount={11}
          domain={[0, 10 * timeBase]}
        />
        <YAxis yAxisId="left" domain={[-1 * yDomain, yDomain]} />
        <YAxis yAxisId="right" orientation="right" />
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
        {isMicActive && (
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch4"
            stroke="#5e35b1"
            dot={false}
            activeDot={{ r: 4 }}
          />
        )}
      </LineChart>
    </ResponsiveContainer>
  );
};

export default withTheme(Graph);
