import styled from 'styled-components';
import { Card } from '@material-ui/core';

export const SettingsContainer = styled.div`
  width: 100%;
  height: calc(100% - 16px);
  display: flex;
  flex-direction: column;
  margin: 8px 0px 0px 16px;
`;

export const SettingsWrapper = styled(Card)`
  width: calc(100% - 16px);
  margin: 8px 0px;
`;

export const OptionsRowWrapper = styled.div`
  display: flex;
  align-items: center;
  margin: 16px 0px 16px 16px;
  min-width: 80%;
`;
