import React from 'react';
import BackLayoutImg from '../../resources/back_layout.png';
import { ImageContainer } from './styles';

const BackLayout = () => {
  return (
    <div
      style={{
        height: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <ImageContainer>
        <img src={BackLayoutImg}></img>
      </ImageContainer>
    </div>
  );
};

export default BackLayout;
