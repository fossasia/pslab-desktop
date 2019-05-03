import React from 'react';
import { Card, Checkbox, Select, Slider } from 'antd';
import { Scrollbars } from 'react-custom-scrollbars';
import {
  SettingsContainer,
  SettingsWrapper,
  OptionsRowWrapper,
} from './Settings.styles';
import { options } from './settingOptions';

const { Option } = Select;

const Settings = props => {
  return (
    <SettingsContainer>
      <Scrollbars autoHide autoHideTimeout={1000}>
        <SettingsWrapper>
          <Card style={{ marginBottom: 8 }} title="Channel Parameters">
            <OptionsRowWrapper>
              <Checkbox>CH1</Checkbox>
              <div>
                <span style={{ marginRight: 4 }}>Range</span>
                <Select defaultValue="16" style={{ width: 100 }}>
                  {Object.entries(options.Range1).map(el => {
                    const key = el[0];
                    const value = el[1];
                    return <Option value={key}>{value}</Option>;
                  })}
                </Select>
              </div>
              <Select defaultValue="CH1" style={{ width: 80 }}>
                {Object.entries(options.Channel1).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <Checkbox>CH2</Checkbox>
              <div>
                <span style={{ marginRight: 4 }}>Range</span>
                <Select defaultValue="16" style={{ width: 100 }}>
                  {Object.entries(options.Range1).map(el => {
                    const key = el[0];
                    const value = el[1];
                    return <Option value={key}>{value}</Option>;
                  })}
                </Select>
              </div>
              <Select defaultValue="CH" style={{ width: 80 }} disabled>
                <Option value="CH">CH2</Option>
              </Select>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <Checkbox>CH3(+/- 3.3V)</Checkbox>
              <Checkbox>Mic</Checkbox>
              <Select defaultValue="Select Mic" style={{ width: 120 }}>
                {Object.entries(options.Mic).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
        <SettingsWrapper>
          <Card style={{ marginBottom: 8 }} title="Timebase and Trigger">
            <OptionsRowWrapper>
              <span style={{ marginRight: 4 }}>TimeBase</span>
              <Slider defaultValue={30} tipFormatter={value => `${value}s`} />
              100 s
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <Checkbox>Trigger</Checkbox>
              <Select defaultValue="CH1" style={{ width: 100 }}>
                {Object.entries(options.Select).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
              <Slider defaultValue={30} tipFormatter={value => `${value}s`} />V
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
        <SettingsWrapper>
          <Card style={{ marginBottom: 8 }} title="Data Analysis">
            <OptionsRowWrapper>
              <Select defaultValue="Sine" style={{ width: 100 }}>
                {Object.entries(options.FitSelect).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
              <Select defaultValue="None" style={{ width: 100 }}>
                {Object.entries(options.DataAnalysisSelect).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
              <Select defaultValue="None" style={{ width: 100 }}>
                {Object.entries(options.DataAnalysisSelect).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <Checkbox>Fourier Transforms</Checkbox>
            </OptionsRowWrapper>
          </Card>
        </SettingsWrapper>
        <SettingsWrapper>
          <Card title="XY Plot">
            <OptionsRowWrapper>
              <Checkbox>Enable XY Plot</Checkbox>
            </OptionsRowWrapper>
            <OptionsRowWrapper>
              <Select defaultValue="CH1" style={{ width: 100 }}>
                {Object.entries(options.Select).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
                })}
              </Select>
              <Select defaultValue="CH2" style={{ width: 100 }}>
                {Object.entries(options.Select).map(el => {
                  const key = el[0];
                  const value = el[1];
                  return <Option value={key}>{value}</Option>;
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
