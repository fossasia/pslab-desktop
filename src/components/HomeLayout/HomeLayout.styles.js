import styled from 'styled-components';

export const LayoutContainer = styled.div`
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  justify-content: center;
  align-items: center;
  background: ${props => props.theme.background.default};
`;
