import styled from 'styled-components';

export const CustomCard = styled.div`
  position: relative;
  display: flex;
  width: 48em;
  height: 26em;
  margin-right: 1em;
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

  @media only screen and (max-width: 1800px) {
    margin-top: 10px;
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

export const HorizontalBar = styled.div`
  width: 74%;
  height: 2em;
  z-index: 1;
  bottom: 5.5em;
  left: 0px;
  position: absolute;
  border-style: solid;
  border-color: #fff;
  border-width: 4px 0px 4px 0px;
  clip-path: polygon(0 0, 96% 0, 100% 100%, 0 100%);
`;

export const VerticalBar = styled.div`
  width: 2em;
  height: 52.5%;
  z-index: 1;
  top: 0px;
  right: 5.5em;
  position: absolute;
  border-style: solid;
  border-color: #fff;
  border-width: 0px 4px 0px 4px;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 89%);
`;
