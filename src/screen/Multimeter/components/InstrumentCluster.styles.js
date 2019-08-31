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
  justify-content: flex-start;
  margin: 0px 0px 0px 32px;
`;

export const Backdrop = styled.div`
  position: absolute;
  height: 590px;
  width: 432px;
  display: flex;
  flex-direction: column;
`;

export const TopSection = styled.div`
  height: 226px;
  margin: 16px 16px 4px 16px;
  border: 3px solid red;
  border-radius: 4px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  font-size: 18px;
  color: red;
  padding: 8px 0px 0px 0px;
`;

export const BottomSection = styled.div`
  flex: 1;
  display: flex;
`;

export const ResSection = styled.div`
  margin: 4px 16px 16px 4px;
  border: 3px solid black;
  border-radius: 4px;
  width: 100px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  font-size: 18px;
  color: black;
  padding: 0px 0px 8px 0px;
`;

export const WaveSection = styled.div`
  margin: 4px 4px 16px 16px;
  border: 3px solid black;
  border-radius: 4px;
  flex: 1;
`;
