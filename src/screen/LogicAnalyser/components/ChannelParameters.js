import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {
  Select,
  Typography,
  Divider,
  MenuItem,
  OutlinedInput,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import { withStyles, withTheme } from '@material-ui/core/styles';
import { SettingsWrapper, OptionsRowWrapper } from './Settings.styles';
import { options } from './settingOptions';

const styles = () => ({
  formControl: {
    margin: '0px 16px 0px 0px',
  },
  slider: {
    margin: '0px 8px 0px 0px',
  },
});

class ChannelParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      triggerLabelWidth: 0,
    };
  }

  componentDidMount() {
    this.setState({
      triggerLabelWidth: ReactDOM.findDOMNode(this.triggerRef).offsetWidth,
    });
  }

  render() {
    const { triggerChannel, onChangeTriggerChannel, classes } = this.props;
    const { triggerLabelWidth } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Channel Selection
        </Typography>
        <Divider />
        <OptionsRowWrapper>
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel
              ref={ref => {
                this.triggerRef = ref;
              }}
              htmlFor="outlined-trigger-channel"
            >
              Channel
            </InputLabel>
            <Select
              value={triggerChannel}
              onChange={onChangeTriggerChannel}
              input={
                <OutlinedInput
                  labelWidth={triggerLabelWidth}
                  name="trigger-channel"
                  id="outlined-trigger-channel"
                />
              }
            >
              {Object.entries(options.Select).map((item, index) => {
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

export default withTheme()(withStyles(styles)(ChannelParameters));
