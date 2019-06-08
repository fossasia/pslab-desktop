import styled from 'styled-components';

export const PanelContainer = styled.div`
  display: flex;

  & > * + * {
    margin: 0px 0px 0px 16px;
  }
`;

export const ValueWrapper = styled.div`
  min-width: 6em;
  display: flex;
  flex-direction: column;
  margin: 16px 16px 16px 16px;
  align-items: center;
  justify-content: center;
  cursor: pointer;

  & > * + * {
    margin: 8px 0px 0px 0px;
  }
`;

export const DisplayContainer = styled.div`
  display: flex;
`;
