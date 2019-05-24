import styled from 'styled-components';

export const DialContainer = styled.div`
  position: relative;
  margin: 16px;
  display: flex;
  width: 400px;
  height: 400px;
  z-index: 999;

  & > * {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
    z-index: 9999;
  }
`;

export const DialWrapper = styled.div`
  z-index: 999;
`;

export const IconWrapper = styled.div`
  min-width: 58px;
  min-height: 58px;
`;
