import React from 'react';
import GraphPanelLayout from '../../components/GraphPanelLayout';
import Graph from './components/Graph';
import ActionButtons from './components/ActionButtons';
import Settings from './components/Settings';

const Oscilloscope = () => {
	return (
		<GraphPanelLayout
			settings={<Settings />}
			actionButtons={<ActionButtons />}
			graph={<Graph />}
		/>
	);
};

export default Oscilloscope;
