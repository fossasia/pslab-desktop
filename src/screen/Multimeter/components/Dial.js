import React from 'react';
import { DialContainer, IconWrapper, DialWrapper } from './Dial.styles';
import CustomCircularInput from '../../../components/CustomCircularInput';

const Dial = ({ options, value, onChangeDial }) => {
  return (
    <DialContainer>
      {options.map((item, index) => {
        return (
          <IconWrapper
            key={index}
            style={{
              transform: item.transform,
            }}
          >
            {item.icon}
          </IconWrapper>
        );
      })}
      <DialWrapper>
        <CustomCircularInput
          steps={0.01}
          setValue={onChangeDial}
          value={value}
          radius={120}
          min={0}
          max={360}
          step={32.7}
          selector={true}
        />
      </DialWrapper>
    </DialContainer>
  );
};

export default Dial;
