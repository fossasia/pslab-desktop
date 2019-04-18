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
	componentDidMount() {
		loadBalancer.startBackgroundProcess(ipcRenderer, 'oscilloscope', {
			numberOfSamples: 1000,
			timeGap: 10,
			activeChannels: {
				ch1: true,
				ch2: false,
				ch3: false,
				ch4: false,
			},
			delay: 100,
		});
	}

	componentWillUnmount() {
		loadBalancer.stopBackgroundProcess(ipcRenderer, 'oscilloscope');
	}

	render() {
		return (
			<HashRouter>
				<Appshell>
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
