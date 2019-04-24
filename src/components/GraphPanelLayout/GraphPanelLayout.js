import React from 'react';
import {
  LayoutContainer,
  ButtonContainer,
  ButtonWrapper,
  SettingsContainer,
  SettingsWrapper,
  GraphContainer,
  GraphWrapper,
  ThickBar,
} from './GraphPanelLayout.styles';

const GraphPanelLayout = ({ actionButtons, settings, graph }) => {
  return (
    <LayoutContainer>
      <ThickBar />
      <SettingsContainer>
        <ButtonContainer>
          <ButtonWrapper>{actionButtons}</ButtonWrapper>
        </ButtonContainer>
        <SettingsWrapper>{settings}</SettingsWrapper>
      </SettingsContainer>
      <GraphContainer>
        <GraphWrapper>{graph}</GraphWrapper>
      </GraphContainer>
    </LayoutContainer>
  );
};

export default GraphPanelLayout;
