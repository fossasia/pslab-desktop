import styled from 'styled-components';
import { Card } from '@material-ui/core';

export const Container = styled.div`
  display: flex;
  width: 100%;
  height: 100%;
  justify-content: center;
`;

export const Wrapper = styled.div`
  width: 100%;
  margin: 16px 0px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const CustomCard = styled(Card)`
  width: calc(50% - 32px);
`;

export const ContentWrapper = styled.div`
  width: 100%;
  z-index: 1;
  display: flex;
  flex-direction: column;
  margin: 16px 16px 16px 16px;
  cursor: pointer;
`;

export const SettingMain = styled.div`
  font-size: 16px;
  margin: 0px 0px 4px 0px;
`;

export const SettingSub = styled.div`
  font-size: 12px;
  color: gray;
`;
