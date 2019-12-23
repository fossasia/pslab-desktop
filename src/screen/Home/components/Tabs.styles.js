import styled from 'styled-components';

export const TabsContainer = styled.div`
  height: calc(100% - 16px);
  width: 100%;
`;
export const TabsContainerInner = styled.div`
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  margin: 1em auto;
  justify-content: center;
  padding-left: 1em;
  @media only screen and (min-width: 1176px) {
    justify-content: start;
  }
`;
export const TabsWrapper = styled.div`
  margin: 16px 16px 0px 0px;
  width: 98em;
  display: flex;
  justify-content: flex-start;
  align-items: center;
`;
export const TabsRow = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;
