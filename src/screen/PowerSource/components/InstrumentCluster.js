import React from 'react';
import { Card, Button, Typography, Divider } from '@material-ui/core';
import PlusIcon from '@material-ui/icons/Add';
import MinusIcon from '@material-ui/icons/Remove';
import { withStyles } from '@material-ui/core/styles';
import {
  CardContainer,
  ButtonContainer,
  DisplayContainer,
  CircularInputContainer,
  InstrumentContainer,
  CardColumnWrapper,
  ValueWrapper,
} from './InstrumentCluster.styles';
import Display from '../../../components/Display';
import CustomCircularInput from '../../../components/CustomCircularInput';

const styles = theme => ({
  button: {
    margin: '8px 8px',
  },
});

const Settings = props => {
  const {
    pv1,
    pv2,
    pv3,
    pcs,
    onPressButton,
    onChangeSlider,
    onOpenDialog,
    classes,
  } = props;

  const onCheck = value => {
    return false;
  };

  return (
    <CardContainer>
      <CardColumnWrapper>
        <Card>
          <Typography
            style={{ margin: '8px 0px 8px 24px' }}
            component="h4"
            variant="h4"
          >
            PV1
          </Typography>
          <Divider />
          <InstrumentContainer>
            <CircularInputContainer>
              <CustomCircularInput
                setValue={onChangeSlider('pv1')}
                value={pv1}
                radius={86}
                min={-5}
                max={5}
                step={0.01}
              />
            </CircularInputContainer>
            <DisplayContainer>
              <ValueWrapper
                onClick={onOpenDialog({
                  variant: 'simple-input',
                  title: 'PV1',
                  textTitle: 'Enter Voltage ( -5 to 5 )',
                  onAccept: onChangeSlider('pv1'),
                  onCheck,
                  onCancel: () => {},
                })}
              >
                <Display fontSize={6} value={pv1} unit="V" />
              </ValueWrapper>
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
          <Typography
            style={{ margin: '8px 0px 8px 24px' }}
            component="h4"
            variant="h4"
          >
            PV2
          </Typography>
          <Divider />
          <InstrumentContainer>
            <CircularInputContainer>
              <CustomCircularInput
                setValue={onChangeSlider('pv2')}
                value={pv2}
                radius={86}
                min={-3.3}
                max={3.3}
                step={0.01}
              />
            </CircularInputContainer>
            <DisplayContainer>
              <ValueWrapper>
                <Display fontSize={6} value={pv2} unit="V" />
              </ValueWrapper>
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
          <Typography
            style={{ margin: '8px 0px 8px 24px' }}
            component="h4"
            variant="h4"
          >
            PV3
          </Typography>
          <Divider />
          <InstrumentContainer>
            <CircularInputContainer>
              <CustomCircularInput
                setValue={onChangeSlider('pv3')}
                value={pv3}
                radius={86}
                min={0}
                max={3.3}
                step={0.01}
              />
            </CircularInputContainer>
            <DisplayContainer>
              <ValueWrapper>
                <Display fontSize={6} value={pv3} unit="V" />
              </ValueWrapper>
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
          <Typography
            style={{ margin: '8px 0px 8px 24px' }}
            component="h4"
            variant="h4"
          >
            PCS
          </Typography>
          <Divider />
          <InstrumentContainer>
            <CircularInputContainer>
              <CustomCircularInput
                setValue={onChangeSlider('pcs')}
                value={pcs}
                radius={86}
                min={0}
                max={3.3}
                step={0.01}
              />
            </CircularInputContainer>
            <DisplayContainer>
              <ValueWrapper>
                <Display fontSize={6} value={pcs} unit="mA" />
              </ValueWrapper>
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
