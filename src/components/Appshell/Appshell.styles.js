import styled from 'styled-components';
import theme from '../../theme';

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

export const NavigationContainer = styled.div`
	width: 4em;
	background-color: ${theme.navigationBackground};
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
	background-color: ${theme.navigationBackground};
	color: ${props => (props.selected ? theme.primaryColor : '#ffffff')};
	transition: all 0.5s ease;

	&:hover {
		background-color: ${theme.primaryColorFade};
		color: ${theme.primaryColor};
	}
`;

export const AppIconWrapper = styled.div`
	width: 100%;
	height: 4em;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: ${theme.appIconBackground};
`;

export const TopNavigationWrapper = styled.div``;

export const BottomNavigationWrapper = styled.div``;

export const Spacer = styled.div`
	flex: 1;
`;
