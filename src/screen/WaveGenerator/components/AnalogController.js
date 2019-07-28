import React, { Component } from 'react';
import { Card, Button } from '@material-ui/core';
import Slider from '@material-ui/lab/Slider';
import PlusIcon from '@material-ui/icons/Add';
import MinusIcon from '@material-ui/icons/Remove';
import {
  Wrapper,
  MainContainer,
  DisplayWrapper,
  ControllerWrapper,
  SliderContainer,
  ButtonRow,
  TextWrapper,
  BorderMaker,
  Title,
  SliderWrapper,
  ButtonContainer,
  InformationRow1,
  InformationRow2,
  InformationRow3,
  WaveMarker,
  WaveDetails,
  WaveType,
  InfoList,
  InfoText,
} from './Settings.styles';
import { withStyles, withTheme } from '@material-ui/core/styles';

const styles = theme => ({
  s1colorSwitchBase: {
    color: theme.pallet.s1Color,
    '&$colorChecked': {
      color: theme.pallet.s1Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.s1Color,
      },
    },
  },
  s2colorSwitchBase: {
    color: theme.pallet.s2Color,
    '&$colorChecked': {
      color: theme.pallet.s2Color,
      '& + $colorBar': {
        backgroundColor: theme.pallet.s2Color,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class AnalogController extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activePin: 'wave1',
    };
  }

  render() {
    const { classes, theme } = this.props;
    const { activePin } = this.state;

    return (
      <Card>
        <Wrapper>
          <MainContainer>
            <DisplayWrapper>
              <InformationRow1>
                <WaveMarker active={activePin === 'wave1'}>Wave1</WaveMarker>
                <WaveMarker active={activePin === 'wave2'}>Wave2</WaveMarker>
              </InformationRow1>
              <InformationRow2>
                <WaveType>
                  <InfoText>Sine</InfoText>
                </WaveType>
                <InfoList>
                  <InfoText style={{ margin: '0px 0px 0px 16px' }}>
                    Frequency: 3000Hz
                  </InfoText>
                  <InfoText style={{ margin: '32px 0px 0px 16px' }}>
                    Phase: --
                  </InfoText>
                </InfoList>
              </InformationRow2>
              <InformationRow3>
                <WaveDetails>Wave Frequency : 1000Hz</WaveDetails>
              </InformationRow3>
            </DisplayWrapper>
            <ControllerWrapper>
              <Title>Analog</Title>
              <BorderMaker>
                <ButtonRow>
                  <Button
                    style={{
                      backgroundColor: theme.pallet.primary.main,
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    fullWidth={true}
                  >
                    <TextWrapper>Wave1</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor: theme.pallet.primary.main,
                    }}
                    size="large"
                    color="primary"
                    variant="contained"
                    fullWidth={true}
                  >
                    <TextWrapper>Wave2</TextWrapper>
                  </Button>
                </ButtonRow>
                <ButtonRow>
                  <Button
                    style={{
                      backgroundColor: theme.pallet.primary.main,
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    fullWidth={true}
                  >
                    <TextWrapper>Freq</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor: theme.pallet.primary.main,
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    fullWidth={true}
                  >
                    <TextWrapper>Phase</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor: theme.pallet.primary.main,
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    fullWidth={true}
                  >
                    <TextWrapper>Sine</TextWrapper>
                  </Button>
                </ButtonRow>
              </BorderMaker>
              <ButtonRow>
                <Button
                  style={{
                    backgroundColor: theme.pallet.primary.main,
                  }}
                  size="large"
                  variant="contained"
                  color="primary"
                  fullWidth={true}
                >
                  <TextWrapper>View</TextWrapper>
                </Button>
                <Button
                  size="large"
                  variant="contained"
                  color="primary"
                  fullWidth={true}
                  style={{
                    margin: '0px 0px 0px 16px',
                    backgroundColor: theme.pallet.primary.main,
                  }}
                >
                  <TextWrapper>Mode</TextWrapper>
                </Button>
              </ButtonRow>
            </ControllerWrapper>
          </MainContainer>
          <SliderContainer>
            <SliderWrapper>
              <Slider className={classes.slider} step={1} min={0} max={360} />
            </SliderWrapper>
            <ButtonContainer>
              <Button size="large" color="primary" variant="outlined">
                <MinusIcon style={{ fontSize: 20 }} />
              </Button>
              <Button
                size="large"
                color="primary"
                variant="outlined"
                style={{ margin: '0px 0px 0px 16px' }}
              >
                <PlusIcon style={{ fontSize: 20 }} />
              </Button>
            </ButtonContainer>
          </SliderContainer>
        </Wrapper>
      </Card>
    );
  }
}

export default withTheme()(withStyles(styles)(AnalogController));
