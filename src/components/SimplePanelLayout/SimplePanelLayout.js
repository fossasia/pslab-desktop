import React from 'react';
import { LayoutWrapper, LayoutContainer } from './SimplePanelLayout.styles';

const SimplePanelLayout = props => {
  const { panel } = props;

  return (
    <LayoutContainer>
      {/* <ThickBar /> */}
      <LayoutWrapper>{panel}</LayoutWrapper>
    </LayoutContainer>
  );
};

export default SimplePanelLayout;
