import styled from 'styled-components';

export const CustomCard = styled.div`
  display: flex;
  width: 52em;
  height: 34em;
  transition-timing-function: ease-in-out;
  transition-duration: 200ms;
  border-radius: 8px;
  background-color: ${props => props.theme.primary.main};
  box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.2),
    0px 1px 1px 0px rgba(0, 0, 0, 0.14), 0px 2px 1px -1px rgba(0, 0, 0, 0.12);

  &:hover {
    cursor: pointer;
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2),
      0px 6px 10px 0px rgba(0, 0, 0, 0.14), 0px 1px 18px 0px rgba(0, 0, 0, 0.12);
  }
`;

export const ImageWrapper = styled.div`
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  width: 40em;
  margin: 0px 48px 48px 0px;
`;

export const ContentContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin: 32px 0px 0px 32px;
`;

export const Title = styled.div`
  font-size: 2.8em;
  font-weight: 400;
  color: ${props => props.theme.common.white};
`;

export const Description = styled.div`
  font-size: 1.6em;
  font-weight: 350;
  margin: 32px 0px 0px 0px;
  color: ${props => props.theme.common.white};
`;
