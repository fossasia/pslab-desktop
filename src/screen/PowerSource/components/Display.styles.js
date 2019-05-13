import styled from 'styled-components';

export const ValueContainer = styled.div`
  min-width: 24em;
  display: flex;
  flex-direction: column;
  margin: 16px 16px 16px 16px;
  align-items: center;
  justify-content: center;
`;

export const ValueWrapper = styled.div`
  font-size: 8em;
  color: ${props => props.theme.text.secondary};
`;
