import styled from 'styled-components';

export const CardContainer = styled.div`
  display: flex;
  flex-direction: row;
`;

export const CardColumnWrapper = styled.div`
  display: flex;
  flex-direction: column;

  margin: 0px 0px 0px 32px;

  & > * + * {
    margin: 32px 0px 0px 0px;
  }
`;

export const ButtonContainer = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin: 16px 16px 16px 16px;
`;

export const DisplayContainer = styled.div`
  display: flex;
  flex-direction: column;
`;

export const SliderContainer = styled.div`
  display: flex;
  margin: 8px 0px 16px 32px;
`;

export const InstrumentContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin: 8px;
`;
