import styled from 'styled-components';
import { Card } from '@material-ui/core';

export const SettingsContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  margin: 0px 0px 0px 16px;
`;

export const SettingsWrapper = styled(Card)`
  width: calc(100% - 16px);
  margin: 8px 0px;
`;

export const OptionsRowWrapper = styled.div`
  display: flex;
  align-items: center;
  margin: 16px 16px 16px 16px;
  min-width: 80%;
`;

export const GraphWrapper = styled.div`
  margin: 16px 0px 0px 16px;
  display: flex;
  height: calc(100% - 16px);
  width: calc(100% - 16px);
  background-color: #ffffff;
  border: 1px solid #e8e8e8;
  color: rgba(0, 0, 0, 0.65);
  border-radius: 2px;
`;

export const FixedWrapper = styled.div`
  display: flex;
`;

export const ScrollWrapper = styled.div`
  display: flex;
  flex: 1;
`;
