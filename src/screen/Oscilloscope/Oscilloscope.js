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
		ipcRenderer.on('TO_RENDERER_OSC_DATA', (event, args) => {
			this.setState({
				data: args,
			});
		});
	}

	componentWillUnmount() {
		ipcRenderer.removeAllListeners('TO_RENDERER_OSC_DATA');
	}

	onToggleRead = event => {
		const { isReading, activeChannels } = this.state;
		this.setState(prevState => ({
			isReading: !prevState.isReading
		}));
		if (isReading) {
			loadBalancer.stopBackgroundProcess(ipcRenderer, 'oscilloscope');
		} else {
			loadBalancer.startBackgroundProcess(ipcRenderer, 'oscilloscope', {
				numberOfSamples: 1000,
				timeGap: 10,
				activeChannels,
				delay: 100,
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
