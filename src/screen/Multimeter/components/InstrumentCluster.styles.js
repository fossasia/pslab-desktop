import styled from 'styled-components';

export const InstrumentContainer = styled.div`
  display: flex;
  flex-direction: column;
`;

export const DisplayContainer = styled.div`
  margin: 0px 0px 8px 0px;
`;

export const DisplayWrapper = styled.div`
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 0px 16px 0px 0px;
`;

export const TextIcon = styled.div`
  font-size: 16px;
  font-weight: 900;
  height: 34px;
  width: 34px;
  vertical-align: middle;
  line-height: 34px;
  color: ${props =>
    props.active ? props.theme.secondary.dark : props.theme.text.hint};
`;

export const SwitchWrapper = styled.div`
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin: 0px 16px 0px 0px;
`;
