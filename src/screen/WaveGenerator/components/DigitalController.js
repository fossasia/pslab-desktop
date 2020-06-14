import React, { Component } from 'react';
import { Card, Button } from '@material-ui/core';
import Slider from '@material-ui/core/Slider';
import PlusIcon from '@material-ui/icons/ArrowRight';
import MinusIcon from '@material-ui/icons/ArrowLeft';
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
import PWMIcon from '../../../resources/ic_pwm_pic.png';

const styles = theme => ({
  s1colorSwitchBase: {
    color: theme.palette.s1Color,
    '&$colorChecked': {
      color: theme.palette.s1Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.s1Color,
      },
    },
  },
  s2colorSwitchBase: {
    color: theme.palette.s2Color,
    '&$colorChecked': {
      color: theme.palette.s2Color,
      '& + $colorBar': {
        backgroundColor: theme.palette.s2Color,
      },
    },
  },
  colorBar: {},
  colorChecked: {},
});

class DigitalController extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activePin: 'sqr1',
      activeSetting: 'Freq',
    };
  }

  onChangeSlider = (e, value) => {
    const { onChangeSlider } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activeSetting === 'Freq') {
      return onChangeSlider('pwmFrequency')(e, value);
    }
    if (activePin === 'sqr1') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr1DutyCycle')(e, value);
      }
    } else if (activePin === 'sqr2') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr2DutyCycle')(e, value);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr2Phase')(e, value);
      }
    } else if (activePin === 'sqr3') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr3DutyCycle')(e, value);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr3Phase')(e, value);
      }
    } else if (activePin === 'sqr4') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr4DutyCycle')(e, value);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr4Phase')(e, value);
      }
    }
  };

  onHandlePlus = () => {
    const {
      onChangeSlider,
      pwmFrequency,
      sqr2Phase,
      sqr3Phase,
      sqr4Phase,
      sqr1DutyCycle,
      sqr2DutyCycle,
      sqr3DutyCycle,
      sqr4DutyCycle,
    } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activeSetting === 'Freq') {
      return onChangeSlider('pwmFrequency')(null, pwmFrequency + 1);
    }
    if (activePin === 'sqr1') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr1DutyCycle')(null, sqr1DutyCycle + 1);
      }
    } else if (activePin === 'sqr2') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr2DutyCycle')(null, sqr2DutyCycle + 1);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr2Phase')(null, sqr2Phase + 1);
      }
    } else if (activePin === 'sqr3') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr3DutyCycle')(null, sqr3DutyCycle + 1);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr3Phase')(null, sqr3Phase + 1);
      }
    } else if (activePin === 'sqr4') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr4DutyCycle')(null, sqr4DutyCycle + 1);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr4Phase')(null, sqr4Phase + 1);
      }
    }
  };

  onHandleMinus = () => {
    const {
      onChangeSlider,
      pwmFrequency,
      sqr2Phase,
      sqr3Phase,
      sqr4Phase,
      sqr1DutyCycle,
      sqr2DutyCycle,
      sqr3DutyCycle,
      sqr4DutyCycle,
    } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activeSetting === 'Freq') {
      return onChangeSlider('pwmFrequency')(null, pwmFrequency - 1);
    }
    if (activePin === 'sqr1') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr1DutyCycle')(null, sqr1DutyCycle - 1);
      }
    } else if (activePin === 'sqr2') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr2DutyCycle')(null, sqr2DutyCycle - 1);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr2Phase')(null, sqr2Phase - 1);
      }
    } else if (activePin === 'sqr3') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr3DutyCycle')(null, sqr3DutyCycle - 1);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr3Phase')(null, sqr3Phase - 1);
      }
    } else if (activePin === 'sqr4') {
      if (activeSetting === 'Duty') {
        return onChangeSlider('sqr4DutyCycle')(null, sqr4DutyCycle - 1);
      } else if (activeSetting === 'Phase') {
        return onChangeSlider('sqr4Phase')(null, sqr4Phase - 1);
      }
    }
  };

  sliderValue = () => {
    const {
      pwmFrequency,
      sqr2Phase,
      sqr3Phase,
      sqr4Phase,
      sqr1DutyCycle,
      sqr2DutyCycle,
      sqr3DutyCycle,
      sqr4DutyCycle,
    } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activeSetting === 'Freq') {
      return pwmFrequency;
    }
    if (activePin === 'sqr1') {
      if (activeSetting === 'Duty') {
        return sqr1DutyCycle;
      }
    } else if (activePin === 'sqr2') {
      if (activeSetting === 'Duty') {
        return sqr2DutyCycle;
      } else if (activeSetting === 'Phase') {
        return sqr2Phase;
      }
    } else if (activePin === 'sqr3') {
      if (activeSetting === 'Duty') {
        return sqr3DutyCycle;
      } else if (activeSetting === 'Phase') {
        return sqr3Phase;
      }
    } else if (activePin === 'sqr4') {
      if (activeSetting === 'Duty') {
        return sqr4DutyCycle;
      } else if (activeSetting === 'Phase') {
        return sqr4Phase;
      }
    }
  };

  highlightedInformation = () => {
    const {
      pwmFrequency,
      sqr2Phase,
      sqr3Phase,
      sqr4Phase,
      sqr1DutyCycle,
      sqr2DutyCycle,
      sqr3DutyCycle,
      sqr4DutyCycle,
    } = this.props;
    const { activePin, activeSetting } = this.state;
    if (activeSetting === 'Freq') {
      return `Wave Frequency : ${pwmFrequency}Hz`;
    }
    if (activePin === 'sqr1') {
      if (activeSetting === 'Duty') {
        return `Wave Duty Cycle : ${sqr1DutyCycle}%`;
      }
    } else if (activePin === 'sqr2') {
      if (activeSetting === 'Duty') {
        return `Wave Duty Cycle : ${sqr2DutyCycle}%`;
      } else if (activeSetting === 'Phase') {
        return `Wave Phase Cycle : ${sqr2Phase}°`;
      }
    } else if (activePin === 'sqr3') {
      if (activeSetting === 'Duty') {
        return `Wave Duty Cycle : ${sqr3DutyCycle}%`;
      } else if (activeSetting === 'Phase') {
        return `Wave Phase Cycle : ${sqr3Phase}°`;
      }
    } else if (activePin === 'sqr4') {
      if (activeSetting === 'Duty') {
        return `Wave Duty Cycle : ${sqr4DutyCycle}%`;
      } else if (activeSetting === 'Phase') {
        return `Wave Phase Cycle : ${sqr4Phase}°`;
      }
    }
  };

  render() {
    const {
      classes,
      theme,
      pwmFrequency,
      sqr1DutyCycle,
      sqr2DutyCycle,
      sqr2Phase,
      sqr3DutyCycle,
      sqr3Phase,
      sqr4DutyCycle,
      sqr4Phase,
      onTogglePreview,
    } = this.props;
    const { activePin, activeSetting } = this.state;
    const getMaxSliderValue = () => {
      switch (activeSetting) {
        case 'Freq':
          return 5000;
        case 'Phase':
          // the maximum angle is 360
          return 360;
        default:
          // maximum percentage, used for duty cycle
          return 100;
      }
    };
    return (
      <Card>
        <Wrapper>
          <MainContainer>
            <DisplayWrapper>
              <InformationRow1>
                <WaveMarker active={activePin === 'sqr1'}>SQR1</WaveMarker>
                <WaveMarker active={activePin === 'sqr2'}>SQR2</WaveMarker>
                <WaveMarker active={activePin === 'sqr3'}>SQR3</WaveMarker>
                <WaveMarker active={activePin === 'sqr4'}>SQR4</WaveMarker>
              </InformationRow1>
              <InformationRow2>
                <WaveType>
                  <InfoText>
                    <img src={PWMIcon} alt="" />
                  </InfoText>
                </WaveType>
                <InfoList>
                  <InfoText style={{ margin: '0px 0px 0px 32px' }}>
                    Frequency: {pwmFrequency}Hz
                  </InfoText>
                  <InfoText style={{ margin: '32px 0px 0px 32px' }}>
                    Phase: {activePin === 'sqr1' && '---'}
                    {activePin === 'sqr2' && `${sqr2Phase}°`}
                    {activePin === 'sqr3' && `${sqr3Phase}°`}
                    {activePin === 'sqr4' && `${sqr4Phase}°`}
                  </InfoText>
                  <InfoText style={{ margin: '32px 0px 0px 32px' }}>
                    Duty: {activePin === 'sqr1' && `${sqr1DutyCycle}%`}
                    {activePin === 'sqr2' && `${sqr2DutyCycle}%`}
                    {activePin === 'sqr3' && `${sqr3DutyCycle}%`}
                    {activePin === 'sqr4' && `${sqr4DutyCycle}%`}
                  </InfoText>
                </InfoList>
              </InformationRow2>
              <InformationRow3>
                <WaveDetails>{this.highlightedInformation()}</WaveDetails>
              </InformationRow3>
            </DisplayWrapper>
            <ControllerWrapper>
              <Title>Digital</Title>
              <BorderMaker>
                <ButtonRow>
                  <Button
                    style={{
                      backgroundColor:
                        activePin === 'sqr1'
                          ? '#ef9a9a'
                          : theme.palette.primary.main,
                      color: '#fff',
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() =>
                      this.setState({
                        activePin: 'sqr1',
                        activeSetting: 'Freq',
                      })
                    }
                    disabled={activePin === 'sqr1'}
                  >
                    <TextWrapper>SQR1</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor:
                        activePin === 'sqr2'
                          ? '#ef9a9a'
                          : theme.palette.primary.main,
                      color: '#fff',
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() => this.setState({ activePin: 'sqr2' })}
                    disabled={activePin === 'sqr2'}
                  >
                    <TextWrapper>SQR2</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor:
                        activePin === 'sqr3'
                          ? '#ef9a9a'
                          : theme.palette.primary.main,
                      color: '#fff',
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() => this.setState({ activePin: 'sqr3' })}
                    disabled={activePin === 'sqr3'}
                  >
                    <TextWrapper>SQR3</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor:
                        activePin === 'sqr4'
                          ? '#ef9a9a'
                          : theme.palette.primary.main,
                      color: '#fff',
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() => this.setState({ activePin: 'sqr4' })}
                    disabled={activePin === 'sqr4'}
                  >
                    <TextWrapper>SQR4</TextWrapper>
                  </Button>
                </ButtonRow>
                <ButtonRow>
                  <Button
                    style={{ backgroundColor: theme.palette.primary.main }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() => this.setState({ activeSetting: 'Freq' })}
                  >
                    <TextWrapper>Freq</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor:
                        activePin === 'sqr1'
                          ? '#ef9a9a'
                          : theme.palette.primary.main,
                      color: '#fff',
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() => this.setState({ activeSetting: 'Phase' })}
                    disabled={activePin === 'sqr1'}
                  >
                    <TextWrapper>Phase</TextWrapper>
                  </Button>
                  <Button
                    style={{
                      margin: '0px 0px 0px 16px',
                      backgroundColor: theme.palette.primary.main,
                      color: '#fff',
                    }}
                    size="large"
                    variant="contained"
                    color="primary"
                    className={classes.button}
                    fullWidth={true}
                    onClick={() => this.setState({ activeSetting: 'Duty' })}
                  >
                    <TextWrapper>Duty</TextWrapper>
                  </Button>
                </ButtonRow>
              </BorderMaker>
              <ButtonRow>
                <Button
                  size="large"
                  variant="contained"
                  color="primary"
                  fullWidth={true}
                  style={{
                    margin: '0px 0px 0px 16px',
                    backgroundColor: this.props.wave
                      ? '#ef9a9a'
                      : theme.palette.primary.main,
                    color: '#fff',
                  }}
                  onClick={onTogglePreview}
                  disabled={this.props.wave}
                >
                  <TextWrapper>Analog</TextWrapper>
                </Button>
                <Button
                  size="large"
                  variant="contained"
                  color="primary"
                  fullWidth={true}
                  style={{
                    margin: '0px 0px 0px 16px',
                    backgroundColor: !this.props.wave
                      ? '#ef9a9a'
                      : theme.palette.primary.main,
                    color: '#fff',
                  }}
                  onClick={onTogglePreview}
                  disabled={!this.props.wave}
                >
                  <TextWrapper>Digital</TextWrapper>
                </Button>
              </ButtonRow>
            </ControllerWrapper>
          </MainContainer>
          <SliderContainer>
            <ButtonContainer>
              <Button
                size="large"
                variant="contained"
                className={classes.button}
                onClick={this.onHandleMinus}
                style={{
                  backgroundColor: theme.palette.primary.main,
                  color: '#ffffff',
                  margin: '0px 16px 0px 0px',
                }}
              >
                <MinusIcon style={{ fontSize: 24 }} />
              </Button>
            </ButtonContainer>
            <SliderWrapper>
              <Slider
                value={this.sliderValue()}
                onChange={this.onChangeSlider}
                className={classes.slider}
                step={1}
                min={activeSetting === 'Freq' ? 10 : 0}
                max={getMaxSliderValue()}
              />
            </SliderWrapper>
            <ButtonContainer>
              <Button
                size="large"
                variant="contained"
                className={classes.button}
                style={{
                  margin: '0px 0px 0px 16px',
                  backgroundColor: theme.palette.primary.main,
                  color: '#ffffff',
                }}
                onClick={this.onHandlePlus}
              >
                <PlusIcon style={{ fontSize: 24 }} />
              </Button>
            </ButtonContainer>
          </SliderContainer>
        </Wrapper>
      </Card>
    );
  }
}

export default withTheme(withStyles(styles)(DigitalController));
