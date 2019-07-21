import styled from 'styled-components';

export const KnobCellWrapper = styled.div`
  width: 100%;
  display: flex;
`;

export const KnobCell = styled.div`
  flex: 1;
  border: 1px solid #d9dadb;
  display: flex;
  flex-direction: column;
`;

export const Title = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
`;

export const TitleText = styled.div`
  margin: 16px 0px 16px 16px;
  font-size: 18px;
  color: ${props => props.theme.text.secondary};
`;

export const ButtonWrapper = styled.div`
  margin: 16px 16px 16px 0px;
`;

export const Spacer = styled.div`
  flex: 1;
`;

export const InputWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  margin: 16px 16px 32px 16px;
`;

export const PaintContainer = styled.div`
  display: flex;
  flex-direction: column;
  overflow-x: auto;
`;

export const PaintRow = styled.div`
  display: flex;
  width: 9600px;
`;

export const PaintCell = styled.div`
  background: #000000;
  border: 2px solid #ffffff;
  border-top-color: ${props =>
    props.active ? props.theme.primary.main : '#fff'};
  width: 160px;
  height: 100px;
  display: flex;
  flex-direction: column;
`;

export const ValueWrapper = styled.div`
  width: calc(100% - 32px);
  height: 21px;
  margin: 16px;
  font-size: 28px;
  color: ${props => props.theme.common.white};
`;

export const IndexWrapper = styled.div`
  width: calc(100% - 32px);
  margin: 16px;
  font-size: 14px;
  color: ${props => props.theme.common.white};
  text-align: right;
`;

export const TimeControlPanel = styled.div`
  margin: 4px 0px 4px 0px;
  width: 64px;
  background: ${props => props.theme.primary.main};
  display: flex;
  flex-direction: column;
  justify-content: center;
`;
