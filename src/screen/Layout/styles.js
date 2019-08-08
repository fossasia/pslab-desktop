import styled from 'styled-components';

export const ImageContainer = styled.div`
  position: relative;
`;

export const Marker = styled.div`
  position: absolute;
  top: ${props => props.top}px;
  left: ${props => props.left}px;
  height: 20px;
  width: 20px;
`;
