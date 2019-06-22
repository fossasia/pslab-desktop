import styled from 'styled-components';

export const PanelContainer = styled.div`
  display: flex;
  margin: 16px 0px 0px 16px;
  width: calc(100% - 16px);

  & > * + * {
    margin: 0px 0px 0px 16px;
  }
`;

export const ValueWrapper = styled.div`
  min-width: 5.8em;
  display: flex;
  flex-direction: column;
  margin: 16px 8px;
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
