import styled from 'styled-components';
import { Card } from '@material-ui/core';

export const Container = styled.div`
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  overflow-y: auto;
`;

export const Wrapper = styled(Card)`
  margin: 16px 0px;
  height: 870px;
  width: 95%;
  display: flex;
  flex-direction: column;
  align-items: center;
`;
