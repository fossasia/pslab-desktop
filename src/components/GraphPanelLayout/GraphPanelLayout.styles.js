import styled from 'styled-components';

export const LayoutContainer = styled.div`
  background-color: ${props => props.theme.background.default};
  height: 100%;
  width: 100%;
  z-index: 1;
  display: flex;
`;

export const ThickBar = styled.div`
  position: absolute;
  right: 0;
  top: 4em;
  height: calc((100% - 4em) * 0.2);
  width: calc(100% - 3.5em);
  background: ${props => props.theme.gradient1};
  z-index: 0;
`;

export const GraphContainer = styled.div`
  height: 80%;
  display: flex;
  transform: ${props =>
    props.information ? 'translateY(0%)' : 'translateY(-5%)'};
`;

export const SettingsContainer = styled.div`
  width: 28%;
  display: flex;
  flex-direction: column;
  z-index: 2;
`;

export const ButtonWrapper = styled.div`
  display: flex;
`;

export const SettingsWrapper = styled.div`
  flex: 1;
  display: flex;
`;

export const InformationContainer = styled.div`
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: ${props => (props.information ? 'none' : 'center')};
  z-index: 2;
`;
