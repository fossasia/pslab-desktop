import React from 'react';
import {
  LayoutContainer,
  ButtonContainer,
  ButtonWrapper,
  SettingsContainer,
  SettingsWrapper,
  GraphContainer,
  GraphWrapper,
  InformationContainer,
  InformationWrapper,
  ThickBar,
} from './GraphPanelLayout.styles';

const GraphPanelLayout = ({ actionButtons, settings, graph, information }) => {
  return (
    <LayoutContainer>
      <ThickBar />
      <SettingsContainer>
        <ButtonContainer>
          <ButtonWrapper>{actionButtons}</ButtonWrapper>
        </ButtonContainer>
        <SettingsWrapper>{settings}</SettingsWrapper>
      </SettingsContainer>
      <InformationContainer information={information}>
        <GraphContainer information={information}>
          <GraphWrapper>{graph}</GraphWrapper>
        </GraphContainer>
        <InformationWrapper>{information}</InformationWrapper>
      </InformationContainer>
    </LayoutContainer>
  );
};

export default GraphPanelLayout;
