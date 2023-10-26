import styled from 'styled-components';
import { Card } from '@material-ui/core';

export const ActionButtonsWrapper = styled(Card)`
  width: calc(100% - 16px);
  margin: 16px;
`;

export const ButtonWrapper = styled.div`
  display: flex;
  margin: 16px 16px 0px 16px;
  width: calc(100% - 32px);
  justify-content: center;
  align-items: center;
`;

export const CheckboxWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;
