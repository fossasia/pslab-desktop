import styled from 'styled-components';
import { fade } from '@material-ui/core/styles/colorManipulator';

export const AppshellContainer = styled.div`
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  overflow: hidden;
`;

export const ChildrenContainer = styled.div`
  width: 100%;
  height: 100%;
`;

export const ChildrenWrapper = styled.div`
  width: 100%;
  height: calc(100% - 4em);
`;

export const AppBar = styled.div`
  width: 100%;
  height: 4em;
  display: flex;
  background: ${props => props.theme.primary.main};
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2),
    0px 4px 5px 0px rgba(0, 0, 0, 0.14), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
`;

export const TitleContainer = styled.div``;

export const ButtonContainer = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin: 0px 16px 0px 16px;
  z-index: 999;
`;

export const NavigationContainer = styled.div`
  width: 4em;
  background-color: ${props => props.theme.navigationBackground};
  display: flex;
  flex-direction: column;
  z-index: 999;
`;

export const NavigationTab = styled.div`
  min-width: 100%;
  height: 4em;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background-color: ${props => props.theme.navigationBackground};
  color: ${props => props =>
    props.selected ? props.theme.primary.main : props.theme.common.white};
  transition: all 0.5s ease;

  &:hover {
    background-color: ${props => fade(props.theme.primary.main, 0.1)};
    color: ${props => fade(props.theme.primary.main, 0.5)};
  }
`;

export const AppIconWrapper = styled.div`
  width: 100%;
  height: 4em;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: ${props => props.theme.iconBackground};
`;

export const TopNavigationWrapper = styled.div``;

export const BottomNavigationWrapper = styled.div``;

export const Spacer = styled.div`
  flex: 1;
`;
