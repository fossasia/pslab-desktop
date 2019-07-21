import React from 'react';
import {
  KnobCell,
  KnobCellWrapper,
  Title,
  TitleText,
  Spacer,
  ButtonWrapper,
  InputWrapper,
  TimeControlPanel,
} from './styles';
import IconButton from '@material-ui/core/IconButton';
import {
  Menu as PaintIcon,
  PlayArrow as PlayIcon,
  Stop as StopIcon,
  Pause as PauseIcon,
  Save as SaveIcon,
} from '@material-ui/icons';
import CustomCircularInput from '../../../components/CustomCircularInput';

const KnobControl = ({
  brush1,
  brush2,
  brush3,
  brush4,
  changeBrushValue,
  setActiveBrush,
  start,
  stop,
  pause,
  active,
}) => {
  return (
    <KnobCellWrapper>
      <KnobCell>
        <Title>
          <TitleText>Servo 1</TitleText>
          <Spacer />
          <ButtonWrapper>
            <div
              draggable="true"
              onDragStart={event => setActiveBrush('servo1')}
            >
              <PaintIcon size={28} />
            </div>
          </ButtonWrapper>
        </Title>
        <InputWrapper>
          <CustomCircularInput
            setValue={changeBrushValue('brush1')}
            value={brush1}
            radius={106}
            min={0}
            max={360}
            step={1}
            text={true}
            title="Servo 1"
          />
        </InputWrapper>
      </KnobCell>
      <KnobCell>
        <Title>
          <TitleText>Servo 2</TitleText>
          <Spacer />
          <ButtonWrapper>
            <div
              draggable="true"
              onDragStart={event => setActiveBrush('servo2')}
            >
              <PaintIcon size={28} />
            </div>
          </ButtonWrapper>
        </Title>
        <InputWrapper>
          <CustomCircularInput
            setValue={changeBrushValue('brush2')}
            value={brush2}
            radius={106}
            min={0}
            max={360}
            step={1}
            text={true}
            title="Servo 2"
          />
        </InputWrapper>
      </KnobCell>
      <KnobCell>
        <Title>
          <TitleText>Servo 3</TitleText>
          <Spacer />
          <ButtonWrapper>
            <div
              draggable="true"
              onDragStart={event => setActiveBrush('servo3')}
            >
              <PaintIcon size={28} />
            </div>
          </ButtonWrapper>
        </Title>
        <InputWrapper>
          <CustomCircularInput
            setValue={changeBrushValue('brush3')}
            value={brush3}
            radius={106}
            min={0}
            max={360}
            step={1}
            text={true}
            title="Servo 3"
          />
        </InputWrapper>
      </KnobCell>
      <KnobCell>
        <Title>
          <TitleText>Servo 4</TitleText>
          <Spacer />
          <ButtonWrapper>
            <div
              draggable="true"
              onDragStart={event => setActiveBrush('servo4')}
            >
              <PaintIcon size={28} />
            </div>
          </ButtonWrapper>
        </Title>
        <InputWrapper>
          <CustomCircularInput
            setValue={changeBrushValue('brush4')}
            value={brush4}
            radius={106}
            min={0}
            max={360}
            step={1}
            text={true}
            title="Servo 4"
          />
        </InputWrapper>
      </KnobCell>
      <TimeControlPanel>
        {active ? (
          <IconButton onClick={pause} style={{ color: '#fff' }}>
            <PauseIcon />
          </IconButton>
        ) : (
          <IconButton onClick={start} style={{ color: '#fff' }}>
            <PlayIcon />
          </IconButton>
        )}
        <IconButton
          onClick={stop}
          style={{ margin: '8px 8px 0px 8px', color: '#fff' }}
        >
          <StopIcon />
        </IconButton>
        <IconButton style={{ margin: '8px 8px 0px 8px', color: '#fff' }}>
          <SaveIcon />
        </IconButton>
      </TimeControlPanel>
    </KnobCellWrapper>
  );
};

export default KnobControl;
