import styled from 'styled-components';

export const InstrumentContainer = styled.div`
  display: flex;
`;

export const SwitchContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin: 0px 16px 0px 0px;

  & > * + * {
    margin: 16px 0px 0px 0px;
  }
`;

export const SwitchWrapper = styled.div`
  display: flex;
  flex-direction: column;
  margin: 16px 16px 16px 16px;
`;

export const DisplayContainer = styled.div`
  display: flex;
	margin: 0px 16px 0px 0px;
`;

export const DisplayWrapper = styled.div`
	height: 100%;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
`;
