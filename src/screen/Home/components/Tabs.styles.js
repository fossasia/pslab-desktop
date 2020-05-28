import styled from 'styled-components';

export const TabsContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  margin: 0;
`;

export const TabsRow = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
`;

export const TabsWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
`;

export const InstrumentCard = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  @media only screen and (max-width: 1800px) {
    display: flex;
    flex-direction: wrap;
    justify-content: center;
    align-items: center;
  }
`;
