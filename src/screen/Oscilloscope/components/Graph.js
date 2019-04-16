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

const Graph = ({data, activeChannels}) => {
	return (
		<ResponsiveContainer>
			<LineChart
				data={data}
				margin={{
					top: 48,
					right: 48,
					left: 16,
					bottom: 32,
				}}
			>
				<CartesianGrid strokeDasharray="3 3" />
				<XAxis dataKey="timeGap" type="number" interval="preserveStartEnd"/>
				<YAxis />
				<Tooltip />
				<Legend align="right" iconType="triangle"/>
				{activeChannels['ch1'] && <Line type="monotone" dataKey="ch1" stroke="#8884d8" activeDot={{ r: 8 }} />}
				{activeChannels['ch2'] && <Line type="monotone" dataKey="ch2" stroke="#82ca9d" activeDot={{ r: 8 }} />}
				{activeChannels['ch3'] && <Line type="monotone" dataKey="ch3" stroke="#ff5722" activeDot={{ r: 8 }} />}
				{activeChannels['ch4'] && <Line type="monotone" dataKey="ch4" stroke="#5e35b1" activeDot={{ r: 8 }} />}
			</LineChart>
		</ResponsiveContainer>
	);
};

export default Graph;
