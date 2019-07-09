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

const Graph = ({ activePreview, theme }) => {
  return (
    <ResponsiveContainer>
      <LineChart
        // data={data}
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
          // domain={[0, 10 * timeBase]}
        />
        <YAxis
          yAxisId="left"
          // domain={[-1 * yDomain, yDomain]}
        />
        <YAxis yAxisId="right" orientation="right" />
        <Tooltip />
        <Legend align="right" iconType="triangle" />
        {
          // activePreview.s1 &&
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch1"
            stroke={theme.s1Color}
            dot={false}
            activeDot={{ r: 4 }}
          />
        }
        {
          // activePreview.s2 &&
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch2"
            stroke={theme.s2Color}
            dot={false}
            activeDot={{ r: 4 }}
          />
        }
        {
          // activePreview.sqr1 &&
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch3"
            stroke={theme.sqr1Color}
            dot={false}
            activeDot={{ r: 4 }}
          />
        }
        {
          // activePreview.sqr2 &&
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch4"
            stroke={theme.sqr2Color}
            dot={false}
            activeDot={{ r: 4 }}
          />
        }
        {
          // activePreview.sqr3 &&
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch4"
            stroke={theme.sqr3Color}
            dot={false}
            activeDot={{ r: 4 }}
          />
        }
        {
          // activePreview.sqr4 &&
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="ch4"
            stroke={theme.sqr4Color}
            dot={false}
            activeDot={{ r: 4 }}
          />
        }
      </LineChart>
    </ResponsiveContainer>
  );
};

export default withTheme(Graph);
