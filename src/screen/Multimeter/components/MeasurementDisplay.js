import React, { Component } from 'react';
import { Card, LinearProgress } from '@material-ui/core';
import { DisplayContainer, DisplayWrapper } from './InstrumentCluster.styles';
import Display from '../../../components/Display';
const electron = window.require('electron');
const { ipcRenderer } = electron;

class MeasurementDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      prefix: null,
      data: 0,
    };
  }

  componentDidMount() {
    ipcRenderer.on('TO_RENDERER_DATA', (event, args) => {
      console.log(args);
      this.setState({
        ...args,
      });
    });
  }

  componentWillUnmount() {
    ipcRenderer.removeAllListeners('TO_RENDERER_DATA');
  }

  render() {
    const { isReading, unit } = this.props;
    const { data, prefix } = this.state;

    return (
      <DisplayContainer>
        <Card>
          {isReading && <LinearProgress />}
          <DisplayWrapper>
            <Display
              fontSize={'6'}
              value={data}
              unit={prefix ? `${prefix}${unit}` : unit}
            />
          </DisplayWrapper>
        </Card>
      </DisplayContainer>
    );
  }
}

export default MeasurementDisplay;
