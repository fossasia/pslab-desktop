import React, { Component } from 'react';
import SimplePanelLayout from '../../components/SimplePanelLayout';
import Settings from './components/Settings';
import roundOff from '../../util/arithmetics';

class PowerSouce extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pv1: -5,
      pv2: -3.3,
      pv3: 0,
      pcs: 0,
    };
  }

  onChangeSlider = pinType => value => {
    this.setState({
      [pinType]: value,
    });
  };

  onPressButton = (pinType, isPositive) => event => {
    this.setState({
      [pinType]: roundOff(this.state[pinType] + (isPositive ? 0.01 : -0.01)),
    });
  };

  render() {
    const { pv1, pv2, pv3, pcs } = this.state;

    return (
      <SimplePanelLayout
        panel={
          <Settings
            pv1={pv1}
            pv2={pv2}
            pv3={pv3}
            pcs={pcs}
            onPressButton={this.onPressButton}
            onChangeSlider={this.onChangeSlider}
          />
        }
      />
    );
  }
}

export default PowerSouce;
