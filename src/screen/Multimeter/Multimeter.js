import React, { Component } from 'react';
import SimplePanelLayout from '../../components/SimplePanelLayout';
import InstrumentCluster from './components/InstrumentCluster';
import debounce from 'lodash/debounce';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class Multimeter extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return <SimplePanelLayout panel={<InstrumentCluster />} />;
  }
}

export default Multimeter;
