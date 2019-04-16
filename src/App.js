import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';

import Appshell from './components/Appshell';
import Home from './screen/Home';
import Oscilloscope from './screen/Oscilloscope';
import LogicAnalyser from './screen/LogicAnalyser';
import PowerSource from './screen/PowerSource';
import Settings from './screen/Settings';
import './App.css';

class App extends Component {
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
