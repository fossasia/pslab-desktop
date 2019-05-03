import styled from 'styled-components';

export const ButtonWrapper = styled.div`
  display: flex;
  margin: 0px 0px 16px 0px;
  width: 20em;

  & > * + * {
    margin: 0px 0px 0px 16px;
  }
`;
