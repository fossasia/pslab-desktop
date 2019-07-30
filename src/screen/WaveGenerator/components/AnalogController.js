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
import SineIcon from '../../../resources/ic_sin.png';
import TriaIcon from '../../../resources/ic_triangular.png';

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
      activeSetting: 'Freq',
    };
  }

  onChangeSlider = (e, value) => {
    const { onChangeSlider } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activePin === 'wave1') {
      if (activeSetting === 'Freq') {
        onChangeSlider('s1Frequency')(e, value);
      }
    } else if (activePin === 'wave2') {
      if (activeSetting === 'Freq') {
        onChangeSlider('s2Frequency')(e, value);
      } else if (activeSetting === 'Phase') {
        onChangeSlider('s2Phase')(e, value);
      }
    }
  };

  onHandlePlus = () => {
    const { onChangeSlider, s1Frequency, s2Frequency, s2Phase } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activePin === 'wave1') {
      if (activeSetting === 'Freq') {
        onChangeSlider('s1Frequency')(null, s1Frequency + 1);
      }
    } else if (activePin === 'wave2') {
      if (activeSetting === 'Freq') {
        onChangeSlider('s2Frequency')(null, s2Frequency + 1);
      } else if (activeSetting === 'Phase') {
        onChangeSlider('s2Phase')(null, s2Phase + 1);
      }
    }
  };

  onHandleMinus = () => {
    const { onChangeSlider, s1Frequency, s2Frequency, s2Phase } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activePin === 'wave1') {
      if (activeSetting === 'Freq') {
        onChangeSlider('s1Frequency')(null, s1Frequency - 1);
      }
    } else if (activePin === 'wave2') {
      if (activeSetting === 'Freq') {
        onChangeSlider('s2Frequency')(null, s2Frequency - 1);
      } else if (activeSetting === 'Phase') {
        onChangeSlider('s2Phase')(null, s2Phase - 1);
      }
    }
  };

  sliderValue = () => {
    const { s1Frequency, s2Frequency, s2Phase } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activePin === 'wave1') {
      if (activeSetting === 'Freq') {
        return s1Frequency;
      }
    } else if (activePin === 'wave2') {
      if (activeSetting === 'Freq') {
        return s2Frequency;
      } else if (activeSetting === 'Phase') {
        return s2Phase;
      }
    }
  };

  waveForm = () => {
    const { waveFormS1, waveFormS2 } = this.props;
    const { activePin } = this.state;
    if (activePin === 'wave1') {
      if (waveFormS1 === 'sine') {
        return <img src={SineIcon} />;
      }
      return <img src={TriaIcon} />;
    }
    if (waveFormS2 === 'sine') {
      return <img src={SineIcon} />;
    }
    return <img src={TriaIcon} />;
  };

  waveFormInv = () => {
    const { waveFormS1, waveFormS2 } = this.props;
    const { activePin } = this.state;
    if (activePin === 'wave1') {
      if (waveFormS1 === 'tria') {
        return <img src={SineIcon} />;
      }
      return <img src={TriaIcon} />;
    }
    if (waveFormS2 === 'tria') {
      return <img src={SineIcon} />;
    }
    return <img src={TriaIcon} />;
  };

  highlightedInformation = () => {
    const { activePin, activeSetting } = this.state;
    const { s1Frequency, s2Frequency, s2Phase } = this.props;

    if (activePin == 'wave1') {
      if (activeSetting === 'Freq') {
        return `Wave Frequency : ${s1Frequency}Hz`;
      }
    } else {
      if (activeSetting === 'Freq') {
        return `Wave Frequency : ${s2Frequency}Hz`;
      }
      return `Wave Phase : ${s2Phase}°`;
    }
  };

  render() {
    const {
      classes,
      theme,
      s1Frequency,
      s2Frequency,
      s2Phase,
      onChangeWaveForm,
      onTogglePreview,
    } = this.props;
    const { activePin, activeSetting } = this.state;

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
                  <InfoText>{this.waveForm()}</InfoText>
                </WaveType>
                <InfoList>
                  <InfoText style={{ margin: '0px 0px 0px 16px' }}>
                    Frequency:
                    {activePin === 'wave1' ? s1Frequency : s2Frequency}Hz
                  </InfoText>
                  <InfoText style={{ margin: '32px 0px 0px 16px' }}>
                    Phase: {activePin === 'wave1' ? '---' : `${s2Phase}°`}
                  </InfoText>
                </InfoList>
              </InformationRow2>
              <InformationRow3>
                <WaveDetails>{this.highlightedInformation()}</WaveDetails>
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
                    onClick={() =>
                      this.setState({
                        activePin: 'wave1',
                        activeSetting: 'Freq',
                      })
                    }
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
                    onClick={() => this.setState({ activePin: 'wave2' })}
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
                    onClick={() => this.setState({ activeSetting: 'Freq' })}
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
                    onClick={() => this.setState({ activeSetting: 'Phase' })}
                    disabled={activePin === 'wave1'}
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
                    onClick={
                      activePin === 'wave1'
                        ? () => onChangeWaveForm('waveFormS1')
                        : () => onChangeWaveForm('waveFormS2')
                    }
                  >
                    <TextWrapper>{this.waveFormInv()}</TextWrapper>
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
                  onClick={onTogglePreview}
                >
                  <TextWrapper>Mode</TextWrapper>
                </Button>
              </ButtonRow>
            </ControllerWrapper>
          </MainContainer>
          <SliderContainer>
            <SliderWrapper>
              <Slider
                value={this.sliderValue()}
                onChange={this.onChangeSlider}
                className={classes.slider}
                step={1}
                min={activeSetting == 'Freq' ? 10 : 0}
                max={activeSetting == 'Freq' ? 5000 : 360}
              />
            </SliderWrapper>
            <ButtonContainer>
              <Button
                size="large"
                color="primary"
                variant="outlined"
                onClick={this.onHandleMinus}
              >
                <MinusIcon style={{ fontSize: 20 }} />
              </Button>
              <Button
                size="large"
                color="primary"
                variant="outlined"
                style={{ margin: '0px 0px 0px 16px' }}
                onClick={this.onHandlePlus}
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
