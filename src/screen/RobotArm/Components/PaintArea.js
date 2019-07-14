import React from 'react';
import {
  PaintContainer,
  PaintRow,
  PaintCell,
  ValueWrapper,
  IndexWrapper,
} from './styles';

const PaintArea = ({
  brush1,
  brush2,
  brush3,
  brush4,
  servo1,
  servo2,
  servo3,
  servo4,
  activeBrush,
  setServoValues,
  timeLine,
}) => {
  return (
    <PaintContainer>
      <PaintRow>
        {servo1.map((item, index) => {
          return (
            <div
              key={index}
              onDragEnter={event =>
                activeBrush === 'servo1' &&
                setServoValues(brush1, 'servo1', index)
              }
            >
              <PaintCell
                style={{ borderTopWidth: '6px' }}
                active={timeLine === index}
              >
                <ValueWrapper>{item !== null ? `${item}°` : ' '}</ValueWrapper>
                <IndexWrapper>{`${index + 1}s`}</IndexWrapper>
              </PaintCell>
            </div>
          );
        })}
      </PaintRow>
      <PaintRow>
        {servo2.map((item, index) => {
          return (
            <div
              key={index}
              onDragEnter={() =>
                activeBrush === 'servo2' &&
                setServoValues(brush2, 'servo2', index)
              }
            >
              <PaintCell>
                <ValueWrapper>{item !== null ? `${item}°` : ' '}</ValueWrapper>
                <IndexWrapper>{`${index + 1}s`}</IndexWrapper>
              </PaintCell>
            </div>
          );
        })}
      </PaintRow>
      <PaintRow>
        {servo3.map((item, index) => {
          return (
            <div
              key={index}
              onDragEnter={() =>
                activeBrush === 'servo3' &&
                setServoValues(brush3, 'servo3', index)
              }
            >
              <PaintCell>
                <ValueWrapper>{item !== null ? `${item}°` : ' '}</ValueWrapper>
                <IndexWrapper>{`${index + 1}s`}</IndexWrapper>
              </PaintCell>
            </div>
          );
        })}
      </PaintRow>
      <PaintRow>
        {servo4.map((item, index) => {
          return (
            <div
              key={index}
              onDragEnter={() =>
                activeBrush === 'servo4' &&
                setServoValues(brush4, 'servo4', index)
              }
            >
              <PaintCell>
                <ValueWrapper>{item !== null ? `${item}°` : ' '}</ValueWrapper>
                <IndexWrapper>{`${index + 1}s`}</IndexWrapper>
              </PaintCell>
            </div>
          );
        })}
      </PaintRow>
    </PaintContainer>
  );
};

export default PaintArea;
