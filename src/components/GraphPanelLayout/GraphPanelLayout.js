import React from 'react';
import {
  LayoutContainer,
  ButtonWrapper,
  SettingsContainer,
  SettingsWrapper,
  GraphContainer,
  InformationContainer,
} from './GraphPanelLayout.styles';

const GraphPanelLayout = ({ actionButtons, settings, graph, information }) => {
  return (
    <LayoutContainer>
      {/* <ThickBar /> */}
      <InformationContainer information={information}>
        <GraphContainer information={information}>{graph}</GraphContainer>
        {information}
      </InformationContainer>
      <SettingsContainer>
        <ButtonWrapper>{actionButtons}</ButtonWrapper>
        <SettingsWrapper>{settings}</SettingsWrapper>
      </SettingsContainer>
    </LayoutContainer>
  );
};

export default GraphPanelLayout;
