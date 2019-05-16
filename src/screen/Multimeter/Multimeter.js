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
    this.state = {
      isReading: false,
      data: 0,
      unit: 'V',
      activeOption: 'CH1',
      dialValue: 0,
    };
  }

  onChangeDial = value => {
    const dialValue = Math.round(value);
    let activeOption = null;
    console.log(dialValue);
    switch (dialValue) {
      case 0:
        activeOption = 'CH1';
        break;
      case 360:
        activeOption = 'CH1';
        break;
      case 33:
        activeOption = 'CAPACITOR';
        break;
      case 65:
        activeOption = 'RESISTOR';
        break;
      case 98:
        activeOption = 'ID4';
        break;
      case 131:
        activeOption = 'ID3';
        break;
      case 164:
        activeOption = 'ID2';
        break;
      case 196:
        activeOption = 'ID1';
        break;
      case 229:
        activeOption = 'AN8';
        break;
      case 262:
        activeOption = 'CAP';
        break;
      case 294:
        activeOption = 'CH3';
        break;
      case 327:
        activeOption = 'CH2';
        break;
      default:
        break;
    }
    this.setState({
      dialValue,
      activeOption,
    });
  };

  onClickButton = (optionName, unit, dialValue) => () => {
    this.setState({
      activeOption: optionName,
      unit,
      dialValue,
    });
  };

  render() {
    const { activeOption, data, unit, dialValue } = this.state;

    return (
      <SimplePanelLayout
        panel={
          <InstrumentCluster
            activeOption={activeOption}
            onClickButton={this.onClickButton}
            onChangeDial={this.onChangeDial}
            data={data}
            unit={unit}
            dialValue={dialValue}
          />
        }
      />
    );
  }
}

export default Multimeter;
