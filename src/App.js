import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';

import Appshell from './components/Appshell';
import Home from './screen/Home';
import Oscilloscope from './screen/Oscilloscope';
import LogicAnalyser from './screen/LogicAnalyser';
import PowerSource from './screen/PowerSource';
import Settings from './screen/Settings';
import './App.css';
const electron = window.require('electron');
const ipcRenderer = electron.ipcRenderer;
const loadBalancer = window.require('electron-load-balancer');

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			isConnected: false,
		};
	}

	onConnectToggle = () => {
		const { isConnected } = this.state;
		if (!isConnected) {
			loadBalancer.startBackgroundProcess(ipcRenderer, 'linker');
		} else {
			loadBalancer.stopBackgroundProcess(ipcRenderer, 'linker');
		}
		this.setState({
			isConnected: !isConnected,
		});
	};

	componentDidMount() {
		ipcRenderer.on('TO_RENDERER_STATUS', (event, args) => {
			const { isConnected } = args;
			this.setState({
				isConnected,
			});
			!isConnected && loadBalancer.stopBackgroundProcess(ipcRenderer, 'linker');
		});
		loadBalancer.startBackgroundProcess(ipcRenderer, 'linker');
	}

	componentWillUnmount() {
		ipcRenderer.removeAllListeners('TO_RENDERER_STATUS');
		loadBalancer.stopBackgroundProcess(ipcRenderer, 'linker');
	}

	render() {
		const { isConnected } = this.state;

		return (
			<HashRouter>
				<Appshell isConnected={isConnected} onConnectToggle={this.onConnectToggle}>
					<Switch>
						<Route path="/" exact component={Home} />
						<Route path="/oscilloscope" exact component={Oscilloscope} />
						<Route path="/logicanalyser" exact component={LogicAnalyser} />
						<Route path="/powersource" exact component={PowerSource} />
						<Route path="/settings" exact component={Settings} />
					</Switch>
				</Appshell>
			</HashRouter>
		);
	}
}

export default App;
