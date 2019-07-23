import styled from 'styled-components';
import { Card } from '@material-ui/core';

export const SettingsContainer = styled.div`
  width: 100%;
  height: calc(100% - 16px);
  display: flex;
  flex-direction: column;
  margin: 8px 0px 0px 16px;
`;

export const SettingsWrapper = styled(Card)`
  width: calc(100% - 16px);
  margin: 8px 0px;
`;

export const OptionsRowWrapper = styled.div`
  display: flex;
  align-items: center;
  margin: 16px 16px 16px 16px;
  min-width: 80%;
`;

export const TitleWrapper = styled.div`
  display: flex;
`;

export const Spacer = styled.div`
  flex: 1;
`;

export const Wrapper = styled.div``;

export const MainContainer = styled.div`
  display: flex;
`;

export const DisplayWrapper = styled.div`
  width: 650px;
  height: 500px;
  margin: 16px 0px 0px 16px;
  background: #000;
  display: flex;
  flex-direction: column;
`;

export const InformationRow1 = styled.div`
  display: flex;
  border-bottom: 1px solid #fff;
`;

export const InformationRow2 = styled.div`
  display: flex;
  flex: 1;
`;

export const InformationRow3 = styled.div`
  display: flex;
  border-top: 1px solid #fff;
`;

export const WaveMarker = styled.div`
  height: 100px;
  color: ${props => (props.active ? '#ffcc80' : '#fff')};
  flex: 1;
  text-align: center;
  font-size: 18px;
  line-height: 100px;
  vertical-align: middle;
`;

export const WaveDetails = styled.div`
  height: 100px;
  color: #ffcc80;
  flex: 1;
  text-align: center;
  font-size: 24px;
  line-height: 100px;
  vertical-align: middle;
`;

export const WaveType = styled.div`
  width: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  margin: 0px 16px;
`;

export const InfoList = styled.div`
  display: flex;
  flex-direction: column;
  flex: 1;
  border-left: 1px solid #fff;
  font-size: 22px;
  justify-content: center;
`;

export const InfoText = styled.div`
  color: #fff;
  text-align: left;
`;

export const ControllerWrapper = styled.div`
  display: flex;
  flex-direction: column;
  margin: 16px;
`;

export const ButtonRow = styled.div`
  display: flex;
  margin: 16px 16px;
`;

export const TextWrapper = styled.div`
  font-size: 20px;
`;

export const Title = styled.div`
  color: ${props => props.theme.primary.main};
  font-size: 24px;
  text-align: center;
`;

export const BorderMaker = styled.div`
  border: 2px solid;
  border-color: ${props => props.theme.primary.main};
  border-radius: 4px;
  padding: 16px 8px;
`;

export const SliderContainer = styled.div`
  height: 40px;
  margin: 16px;
  display: flex;
  align-items: center;
`;

export const SliderWrapper = styled.div`
  height: 10px;
  margin: 0px 0px 0px 16px;
  flex: 1;
`;

export const ButtonContainer = styled.div`
  margin: 0px 0px 0px 16px;
`;
