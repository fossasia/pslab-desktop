import styled from 'styled-components';
import theme from '../../theme';

export const ThickBar = styled.div`
	position: absolute;
	right: 0;
	top: 0;
	height: 30%;
	width: calc(100% - 3.5em);
	background: ${theme.gradient};
	z-index: 0;
`;

export const LayoutContainer = styled.div`
	background-color: ${theme.primaryBackground};
	height: 100%;
	width: 100%;
	z-index: 1;
	display: flex;
`;

export const ButtonContainer = styled.div`
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: flex-end;
`;

export const ButtonWrapper = styled.div``;

export const SettingsContainer = styled.div`
  width: 30em;
  display: flex;
  flex-direction: column;
`;

export const SettingsWrapper = styled.div`
  flex: 1;
  display: flex;
`;

export const GraphContainer = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-end;
`;

export const GraphWrapper = styled.div`
  margin: 0px 16px 0px 0px;
  display: flex;
  height: 80%;
  width: 100%;
  background-color: #ffffff;
  z-index: 1;
  border: 1px solid #e8e8e8;
  color: rgba(0,0,0,0.65);
  border-radius: 2px;
`;
