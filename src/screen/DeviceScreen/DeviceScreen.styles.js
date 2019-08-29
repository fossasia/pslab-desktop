import styled from 'styled-components';

export const Container = styled.div`
  width: 100%;
  height: calc(100vh - 52px);
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const Steps = styled.div`
  display: flex;
  flex-direction: column;
  font-size: 16px;
  margin: 0px 0px 16px 0px;
  width: 310px;
`;

export const Hr = styled.hr`
  width: 35%;
`;

export const Link = styled.div`
  color: red;
  font-size: 24px;
  margin: 20px 0px 0px 0px;

  &:hover {
    cursor: pointer;
  }
`;
