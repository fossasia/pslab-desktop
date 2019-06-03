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
import { withStyles } from '@material-ui/core/styles';
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

class TimeParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      idLabelWidth: 0,
      triggerEdge: 0,
    };
  }

  componentDidMount() {
    this.setState({
      idLabelWidth: ReactDOM.findDOMNode(this.idRef).offsetWidth,
      triggerEdge: ReactDOM.findDOMNode(this.edgeRef).offsetWidth,
    });
  }

  render() {
    const {
      channelID,
      onChangeID,
      edgeSelection,
      onEdgeChange,
      classes,
    } = this.props;
    const { idLabelWidth, triggerEdge } = this.state;

    return (
      <SettingsWrapper>
        <Typography style={{ padding: '0.6rem' }} component="h6" variant="h6">
          Settings
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
                this.idRef = ref;
              }}
              htmlFor="outlined-id-channel"
            >
              Channel
            </InputLabel>
            <Select
              value={channelID}
              onChange={onChangeID}
              input={
                <OutlinedInput
                  labelWidth={idLabelWidth}
                  name="id-channel"
                  id="outlined-id-channel"
                />
              }
            >
              {Object.entries(options.ID).map((item, index) => {
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

        <OptionsRowWrapper>
          <FormControl
            variant="outlined"
            fullWidth={true}
            className={classes.formControl}
          >
            <InputLabel
              ref={ref => {
                this.edgeRef = ref;
              }}
              htmlFor="outlined-edge-channel"
            >
              Edge
            </InputLabel>
            <Select
              value={edgeSelection}
              onChange={onEdgeChange}
              input={
                <OutlinedInput
                  labelWidth={triggerEdge}
                  name="edge-selection"
                  id="outlined-edge-selection"
                />
              }
            >
              {Object.entries(options.Edge).map((item, index) => {
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

export default withStyles(styles)(TimeParameters);
