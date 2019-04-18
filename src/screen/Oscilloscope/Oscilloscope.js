import React, { Component } from 'react';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';
const electron = window.require('electron');
const ipcRenderer = electron.ipcRenderer;
const loadBalancer = window.require('electron-load-balancer');

class Oscilloscope extends Component {
	constructor(props) {
		super(props);
		this.state = {
			isReading: false,
			activeChannels: {
				ch1: true,
				ch2: false,
				ch3: false,
				ch4: false,
			},
			data: [],
		};
	}

	componentDidMount() {
		ipcRenderer.on('TO_RENDERER_DATA', (event, args) => {
			this.setState({
				data: args,
			});
			console.log(args);
		});

		ipcRenderer.on('DEBUG', (event, args) => {
			console.log(args);
		});
	}

	componentWillUnmount() {
		ipcRenderer.removeAllListeners('TO_RENDERER_DATA');
	}

	onToggleRead = event => {
		const { isReading, activeChannels } = this.state;
		this.setState(prevState => ({
			isReading: !prevState.isReading,
		}));
		if (isReading) {
			loadBalancer.send(ipcRenderer, 'oscilloscope', {
				command: 'STOP_OSC',
			});
		} else {
			loadBalancer.send(ipcRenderer, 'oscilloscope', {
				command: 'START_OSC',
				timeGap: 10,
				numberOfSamples: 5000,
				delay: 50,
				ch1: activeChannels['ch1'],
				ch2: activeChannels['ch2'],
				ch3: activeChannels['ch3'],
				ch4: activeChannels['ch4'],
			});
		}
	};

	render() {
		const { data, activeChannels, isReading } = this.state;
		return (
			<GraphPanelLayout
				settings={<Settings />}
				actionButtons={
					<ActionButtons isReading={isReading} onToggleRead={this.onToggleRead} />
				}
				graph={<Graph data={data} activeChannels={activeChannels} />}
			/>
		);
	}
}

export default Oscilloscope;
