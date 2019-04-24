import React from 'react';
import {
  Card,
  Checkbox,
  Select,
  Typography,
  Divider,
  FormControlLabel,
  MenuItem,
} from '@material-ui/core';
import { Slider } from 'antd';
import { Scrollbars } from 'react-custom-scrollbars';
import {
  SettingsContainer,
  SettingsWrapper,
  OptionsRowWrapper,
} from './Settings.styles';
import { options } from './settingOptions';

const Settings = props => {
  return (
    <SettingsContainer>
      <Scrollbars autoHide autoHideTimeout={1000}>
        <SettingsWrapper>
          <Card style={{ margin: '8px 0px' }}>
            <Typography
              style={{ padding: '0.6rem' }}
              component="h6"
              variant="h6"
            >
              Channel Parameters
            </Typography>
            <Divider />
            <OptionsRowWrapper>
              <FormControlLabel control={<Checkbox />} label="CH1" />
              <div>
                <span style={{ marginRight: 4 }}>Range</span>
                <Select style={{ width: 100 }}>
                  {Object.entries(options.Range1).map(el => {
                    const key = el[0];
                    const value = el[1];
                    return <MenuItem value={key}>{value}</MenuItem>;
                  })}
                </Select>
              </div>
              <Select defaultValue="CH1" style={{ width: 80 }}>
                {Object.entries(options.Channel1).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <FormControlLabel control={<Checkbox />} label="CH2" />
              <div>
                <span style={{ marginRight: 4 }}>Range</span>
                <Select style={{ width: 100 }}>
                  {Object.entries(options.Range1).map(el => {
                    const key = el[0];
                    const value = el[1];
                    return <MenuItem value={key}>{value}</MenuItem>;
                  })}
                </Select>
              </div>
              <Select style={{ width: 80 }}>
                <MenuItem value="CH2">CH2</MenuItem>
              </Select>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <FormControlLabel control={<Checkbox />} label="CH3(+/- 3.3V)" />
              <FormControlLabel control={<Checkbox />} label="Mic" />
              <Select style={{ width: 120 }}>
                {Object.entries(options.Mic).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
        <SettingsWrapper>
          <Card style={{ margin: '8px 0px' }}>
            <Typography
              style={{ padding: '0.6rem' }}
              component="h6"
              variant="h6"
            >
              Timebase and Trigger
            </Typography>
            <Divider />
            <OptionsRowWrapper>
              <span style={{ marginRight: 4 }}>TimeBase</span>
              <Slider defaultValue={30} tipFormatter={value => `${value}s`} />
              100 s
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <FormControlLabel control={<Checkbox />} label="Trigger" />
              <Select style={{ width: 100 }}>
                {Object.entries(options.Select).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
              <Slider defaultValue={30} tipFormatter={value => `${value}s`} />V
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
        <SettingsWrapper>
          <Card style={{ margin: '8px 0px' }}>
            <Typography
              style={{ padding: '0.6rem' }}
              component="h6"
              variant="h6"
            >
              Data Analysis
            </Typography>
            <Divider />
            <OptionsRowWrapper>
              <Select style={{ width: 100 }}>
                {Object.entries(options.FitSelect).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
              <Select style={{ width: 100 }}>
                {Object.entries(options.DataAnalysisSelect).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
              <Select style={{ width: 100 }}>
                {Object.entries(options.DataAnalysisSelect).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <FormControlLabel
                control={<Checkbox />}
                label="Fourier Transforms"
              />
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
        <SettingsWrapper>
          <Card style={{ margin: '8px 0px' }}>
            <Typography
              style={{ padding: '0.6rem' }}
              component="h6"
              variant="h6"
            >
              XY Plot
            </Typography>
            <Divider />
            <OptionsRowWrapper>
              <FormControlLabel control={<Checkbox />} label="Enable XY Plot" />
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <Select style={{ width: 100 }}>
                {Object.entries(options.Select).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
              <Select style={{ width: 100 }}>
                {Object.entries(options.Select).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <MenuItem value={key}>{value}</MenuItem>;
                })}
              </Select>
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
      </Scrollbars>
    </SettingsContainer>
  );
};

export default Settings;
