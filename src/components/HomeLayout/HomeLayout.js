import React from 'react';
import { LayoutContainer } from './HomeLayout.styles';

const HomeLayout = ({ title, tabs }) => {
  return <LayoutContainer>{tabs}</LayoutContainer>;
};

export default HomeLayout;
