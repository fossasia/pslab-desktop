import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {
  Select,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';

const styles = theme => ({
  formControl: {
    margin: '0px 0px 0px 16px',
  },
});

class NumberParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      numberOfChannelLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      numberOfChannelLabelWidth: ReactDOM.findDOMNode(this.numberOfChannelRef)
        .offsetWidth,
    });
  }

  render() {
    const { numberOfChannels, changeNumberOfChannels } = this.props;
    const { numberOfChannelLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <OptionsRowWrapper>
          <FormControl variant="outlined" fullWidth={true}>
            <InputLabel
              ref={ref => {
                this.numberOfChannelRef = ref;
              }}
              htmlFor="outlined-number-of-channels"
            >
              Number of Channels
            </InputLabel>
            <Select
              value={numberOfChannels}
              onChange={changeNumberOfChannels}
              input={
                <OutlinedInput
                  labelWidth={numberOfChannelLabelWidth}
                  name="outlined-number-of-channels"
                  id="outlined-number-of-channels"
                />
              }
            >
              {Object.entries(options.NumberOfChannels).map((item, index) => {
                const key = item[0];
                const value = item[1];
                return (
                  <MenuItem key={index} value={key}>
                    {value}
                  </MenuItem>
                );
              })}
            </Select>
          </FormControl>
        </OptionsRowWrapper>
      </SettingsWrapper>
    );
  }
}

export default withStyles(styles)(NumberParameters);
