import React, { Component } from 'react';
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
import { GraphWrapper } from './Settings.styles';

const electron = window.require('electron');
const { ipcRenderer } = electron;

class XYPlotGraph extends Component {
  constructor(props) {
    super(props);
    this.state = {
      xyPlotData: [
        {
          plotChannel1: 0,
          plotChannel2: 0,
        },
      ],
    };
  }

  componentDidMount() {
    ipcRenderer.on('OSC_XY_PLOT_DATA', (event, args) => {
      const { isReading } = this.props;
      isReading &&
        args.data &&
        this.setState({
          xyPlotData: args.data,
        });
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('OSC_XY_PLOT_DATA');
  }

  render() {
    const { theme, plotChannel1, plotChannel2 } = this.props;
    const { xyPlotData } = this.state;

    return (
      <GraphWrapper>
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
      </GraphWrapper>
    );
  }
}

export default withTheme(XYPlotGraph);
