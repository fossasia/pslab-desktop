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

export const LayoutWrapper = styled.div`
	align-self: flex-end;
	margin: 0px 16px 0px 0px;
`;

export const LayoutContainer = styled.div`
	background-color: ${theme.primaryBackground};
	height: 100%;
	width: 100%;
	z-index: 1;
	display: flex;
	flex-direction: column;
	justify-content: center;
`;
