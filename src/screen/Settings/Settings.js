import React, { Component } from 'react';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import {
  Container,
  Wrapper,
  CustomCard,
  ContentWrapper,
  SettingMain,
  SettingSub,
} from './Settings.styles';
import { Scrollbars } from 'react-custom-scrollbars';

class Settings extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isDialogOpen: false,
      dataFormat: 'csv',
    };
    this.activeSetting = null;
  }

  handleChangeDataFormat = event => {
    this.setState({
      dataFormat: event.target.value,
    });
  };

  dialogContentRenderer = () => {
    const { dataFormat } = this.state;
    switch (this.activeSetting) {
      case 'WRITE_TYPE':
        return (
          <div>
            <DialogTitle id="simple-dialog-title">
              Export Data Format
            </DialogTitle>
            <FormControl
              component="fieldset"
              style={{
                margin: '16px',
              }}
            >
              <RadioGroup
                aria-label="data_format"
                name="data_format"
                value={dataFormat}
                onChange={this.handleChangeDataFormat}
                style={{
                  margin: '16px',
                }}
              >
                <FormControlLabel value="csv" control={<Radio />} label="CSV" />
              </RadioGroup>
            </FormControl>
          </div>
        );

      default:
        break;
    }
  };

  handleOpen = type => () => {
    this.setState({
      isDialogOpen: true,
    });
    this.activeSetting = 'WRITE_TYPE';
  };

  handleClose = () => {
    this.setState({
      isDialogOpen: false,
    });
    this.activeSetting = null;
  };

  render() {
    const { isDialogOpen } = this.state;
    return (
      <Container>
        <Dialog onClose={this.handleClose} open={isDialogOpen}>
          {this.dialogContentRenderer()}
        </Dialog>
        <Scrollbars autoHide autoHideTimeout={1000}>
          <Wrapper>
            <CustomCard>
              <ContentWrapper onClick={this.handleOpen('WRITE_TYPE')}>
                <SettingMain>Export Data Format</SettingMain>
                <SettingSub>Current format is CSV format</SettingSub>
              </ContentWrapper>
            </CustomCard>
          </Wrapper>
        </Scrollbars>
      </Container>
    );
  }
}

export default Settings;
