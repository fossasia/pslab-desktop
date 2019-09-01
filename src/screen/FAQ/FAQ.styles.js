import styled from 'styled-components';

export const Container = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  height: calc(100vh - 52px);
  overflow: auto;
  z-index: 0;
`;

export const Wrapper = styled.div`
  width: 50%;
  margin: 16px 0px 0px 0px;
`;

export const Link = styled.span`
  color: #e12b00;

  &:hover {
    cursor: pointer;
  }
`;
