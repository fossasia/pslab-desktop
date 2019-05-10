import React from 'react';
import { Card, Button, Typography, Divider } from '@material-ui/core';
import PlusIcon from '@material-ui/icons/Add';
import MinusIcon from '@material-ui/icons/Remove';
import Slider from '@material-ui/lab/Slider';
import { withStyles } from '@material-ui/core/styles';
import {
  CardContainer,
  ButtonContainer,
  DisplayContainer,
  SliderContainer,
  InstrumentContainer,
  CardColumnWrapper,
} from './Settings.styles';
import Display from './Display';

const styles = theme => ({
  button: {
    margin: '8px 8px',
  },
});

const Settings = props => {
  const { pv1, pv2, pv3, pcs, onPressButton, onChangeSlider, classes } = props;

  return (
    <CardContainer>
      <CardColumnWrapper>
        <Card>
          <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
            PV1
          </Typography>
          <Divider />
          <InstrumentContainer>
            <SliderContainer>
              <Slider
                vertical
                step={0.01}
                value={pv1}
                min={-5}
                max={5}
                onChange={onChangeSlider('pv1')}
              />
            </SliderContainer>
            <DisplayContainer>
              <Display value={pv1} unit="V" />
              <ButtonContainer>
                <Button
                  disabled={pv1 === -5}
                  onClick={onPressButton('pv1', false)}
                  size="large"
                  color="secondary"
                  variant="outlined"
                  className={classes.button}
                >
                  <MinusIcon style={{ fontSize: 20 }} />
                </Button>
                <Button
                  disabled={pv1 === 5}
                  onClick={onPressButton('pv1', true)}
                  color="primary"
                  variant="outlined"
                  size="large"
                  className={classes.button}
                >
                  <PlusIcon style={{ fontSize: 20 }} />
                </Button>
              </ButtonContainer>
            </DisplayContainer>
          </InstrumentContainer>
        </Card>
        <Card>
          <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
            PV2
          </Typography>
          <Divider />
          <InstrumentContainer>
            <SliderContainer>
              <Slider
                vertical
                step={0.01}
                value={pv2}
                min={-3.3}
                max={3.3}
                onChange={onChangeSlider('pv2')}
              />
            </SliderContainer>
            <DisplayContainer>
              <Display value={pv2} unit="V" />
              <ButtonContainer>
                <Button
                  disabled={pv2 === -3.3}
                  onClick={onPressButton('pv2', false)}
                  color="secondary"
                  variant="outlined"
                  size="large"
                  className={classes.button}
                >
                  <MinusIcon style={{ fontSize: 20 }} />
                </Button>
                <Button
                  disabled={pv2 === 3.3}
                  onClick={onPressButton('pv2', true)}
                  color="primary"
                  variant="outlined"
                  size="large"
                  className={classes.button}
                >
                  <PlusIcon style={{ fontSize: 20 }} />
                </Button>
              </ButtonContainer>
            </DisplayContainer>
          </InstrumentContainer>
        </Card>
      </CardColumnWrapper>
      <CardColumnWrapper>
        <Card>
          <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
            PV3
          </Typography>
          <Divider />
          <InstrumentContainer>
            <SliderContainer>
              <Slider
                vertical
                step={0.01}
                value={pv3}
                min={0}
                max={3.3}
                onChange={onChangeSlider('pv3')}
              />
            </SliderContainer>
            <DisplayContainer>
              <Display value={pv3} unit="V" />
              <ButtonContainer>
                <Button
                  disabled={pv3 === 0}
                  onClick={onPressButton('pv3', false)}
                  color="secondary"
                  variant="outlined"
                  size="large"
                  className={classes.button}
                >
                  <MinusIcon style={{ fontSize: 20 }} />
                </Button>
                <Button
                  disabled={pv3 === 3.3}
                  onClick={onPressButton('pv3', true)}
                  color="primary"
                  variant="outlined"
                  size="large"
                  className={classes.button}
                >
                  <PlusIcon style={{ fontSize: 20 }} />
                </Button>
              </ButtonContainer>
            </DisplayContainer>
          </InstrumentContainer>
        </Card>
        <Card title="PCS">
          <Typography style={{ padding: '0.6rem' }} component="h4" variant="h4">
            PCS
          </Typography>
          <Divider />
          <InstrumentContainer>
            <SliderContainer>
              <Slider
                vertical
                step={0.01}
                value={pcs}
                min={0}
                max={3.3}
                onChange={onChangeSlider('pcs')}
              />
            </SliderContainer>
            <DisplayContainer>
              <Display value={pcs} unit="mA" />
              <ButtonContainer>
                <Button
                  disabled={pcs === 0}
                  onClick={onPressButton('pcs', false)}
                  size="large"
                  color="secondary"
                  variant="outlined"
                  className={classes.button}
                >
                  <MinusIcon style={{ fontSize: 20 }} />
                </Button>
                <Button
                  disabled={pcs === 3.3}
                  onClick={onPressButton('pcs', true)}
                  size="large"
                  color="primary"
                  variant="outlined"
                  className={classes.button}
                >
                  <PlusIcon style={{ fontSize: 20 }} />
                </Button>
              </ButtonContainer>
            </DisplayContainer>
          </InstrumentContainer>
        </Card>
      </CardColumnWrapper>
    </CardContainer>
  );
};

export default withStyles(styles)(Settings);
