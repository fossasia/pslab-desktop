import styled from 'styled-components';

export const SettingsContainer = styled.div`
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;

	& > * {
		margin: 16px 16px 0px 16px;
	}
`;

export const SettingsWrapper = styled.div`
	width: calc(100% - 32px);
	height: 100%;
`;