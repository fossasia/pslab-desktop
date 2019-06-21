import React from 'react';
import AppIcon from '../../../resources/app_icon.svg';
import { TitleContainer, TitleWrapper, TextLabel } from './Title.styles';

const Title = () => {
  return (
    <TitleContainer>
      <TitleWrapper>
        <img
          style={{
            height: '8em',
            width: 'auto',
          }}
          alt="App Icon"
          src={AppIcon}
        />
        <TextLabel>Pocket Science Lab</TextLabel>
      </TitleWrapper>
    </TitleContainer>
  );
};

export default Title;
