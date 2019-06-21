import styled from 'styled-components';

export const ThickBar = styled.div`
  position: absolute;
  right: 0;
  top: 4em;
  height: calc((100% - 4em) * 0.2);
  width: calc(100% - 3.5em);
  background: ${props => props.theme.gradient1};
  z-index: 0;
`;

export const LayoutWrapper = styled.div`
  align-self: center;
  z-index: 999;
`;

export const LayoutContainer = styled.div`
  background-color: ${props => props.theme.background.default};
  height: 100%;
  width: 100%;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
`;
