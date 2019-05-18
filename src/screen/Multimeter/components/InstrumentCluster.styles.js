import styled from 'styled-components';

export const InstrumentContainer = styled.div`
  display: flex;
`;

export const DisplayContainer = styled.div`
  display: flex;
  margin: 0px 16px 0px 0px;
`;

export const DisplayWrapper = styled.div`
  width: 480px;
  height: 480px;
  display: flex;
  justify-content: center;
  align-items: center;
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

export const ImageIcon = styled.img`
  height: 34px;
  width: auto;
  color: ${props =>
    props.active ? props.theme.secondary.dark : props.theme.text.hint};
`;
