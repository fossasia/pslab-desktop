import styled from 'styled-components';
import Card from '@material-ui/core/Card';

export const Container = styled.div`
  display: flex;
  width: 100%;
  height: 100%;
  justify-content: center;
`;

export const Wrapper = styled.div`
  width: 100%;
  margin: 16px 0px;
  display: flex;
  flex-direction: column;
  align-items: center;

  & > * + * {
    margin: 16px 0px 0px 0px;
  }
`;

export const CustomCard = styled(Card)`
  width: calc(50% - 32px);
  height: 7.2em;
`;

export const ContentWrapper = styled.div`
  height: 100%;
  width: 100%;
  z-index: 1;
  display: flex;
  justify-content: center;
  cursor: pointer;
`;

export const ButtonContainer = styled.div`
  margin: 0px 16px 0px 0px;
  z-index: 4;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 7.2em;
  width: 7.2em;
`;

export const Spacer = styled.div`
  flex: 1;
`;

export const TextContainer = styled.div`
  height: 7.2em;
  display: flex;
  flex-direction: column;
  margin: 0px 0px 0px 48px;
`;

export const TitleWrapper = styled.div`
  color: ${props => props.theme.text.primary};
  font-size: 1.4em;
  font-weight: 600;
  margin: 16px 0px 0px 0px;
`;

export const InfoContainer = styled.div`
  display: flex;
  color: ${props => props.theme.text.secondary};
  margin: 16px 0px 0px 0px;

  & > * + * {
    margin: 0px 0px 0px 16px;
  }
`;
