import styled from 'styled-components';

export const Container = styled.div`
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const Wrapper = styled.div`
  width: 60%;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: auto;
`;

export const HelpText = styled.div`
  padding: 16px;
  border: 1px solid grey;
  border-radius: 4px;
  margin: 16px 0px 0px 0px;
`;

export const SecondaryContentWrapper = styled.div`
  margin: 16px 0px 0px 0px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const TitleWrapper = styled.div`
  margin: 32px 0px 0px 0px;
  font-size: 1.5em;
  color: ${props => props.theme.text.primary};
`;

export const ScrollWrapper = styled.div`
  margin: 16px 0px 0px 0px;
`;

export const SensorTab = styled.div`
  margin: 16px;
  height: 42px;
  width: 340px;
  display: flex;
  justify-content: center;
  transition-timing-function: ease-in-out;
  transition-duration: 200ms;
  border-radius: 2px;
  background-color: ${props => props.theme.primary.main};
  box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.2),
    0px 1px 1px 0px rgba(0, 0, 0, 0.14), 0px 2px 1px -1px rgba(0, 0, 0, 0.12);

  &:hover {
    cursor: pointer;
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2),
      0px 6px 10px 0px rgba(0, 0, 0, 0.14), 0px 1px 18px 0px rgba(0, 0, 0, 0.12);
  }
`;

export const SensorTitle = styled.div`
  color: ${props => props.theme.common.white};
  font-size: 1.2em;
  font-weight: 600;
  vertical-align: center;
  height: 42px;
  line-height: 42px;
`;
