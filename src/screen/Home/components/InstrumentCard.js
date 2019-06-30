import React from 'react';
import { Link } from 'react-router-dom';
import {
  CustomCard,
  ImageWrapper,
  ContentContainer,
  Title,
  Description,
  HorizontalBar,
  VerticalBar,
} from './InstrumentCard.styles';

const InstrumentCard = ({ icon, title, description, redirectPath }) => {
  return (
    <Link
      to={redirectPath}
      style={{ color: 'inherit', textDecoration: 'inherit' }}
    >
      <CustomCard>
        <ContentContainer>
          <Title>{title}</Title>
          <Description>{description}</Description>
        </ContentContainer>
        <ImageWrapper>{icon}</ImageWrapper>
        <HorizontalBar />
        <VerticalBar />
      </CustomCard>
    </Link>
  );
};

export default InstrumentCard;
