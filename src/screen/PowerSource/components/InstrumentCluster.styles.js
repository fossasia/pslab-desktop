import styled from 'styled-components';

export const CardContainer = styled.div`
  display: flex;
  flex-direction: row;

  & > * + * {
    margin: 0px 0px 0px 32px;
  }
`;

export const CardColumnWrapper = styled.div`
  display: flex;
  flex-direction: column;

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

export const CircularInputContainer = styled.div`
  display: flex;
  margin: 16px 0px 24px 24px;
`;

export const InstrumentContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin: 16px;
`;

export const ValueWrapper = styled.div`
  min-width: 24em;
  display: flex;
  flex-direction: column;
  margin: 16px 16px 16px 16px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
`;
