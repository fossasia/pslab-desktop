import React from 'react';
import { IconButton } from '@material-ui/core';
import { DialContainer, IconWrapper, DialWrapper } from './Dial.styles';
import { withTheme } from 'styled-components';
import CustomCircularInput from '../../../components/CustomCircularInput';
import { iconMap, optionsOrder, angleMap } from './SettingOptions';

const Dial = ({ value, onClickButton, changeOption, activeSubType, theme }) => {
  const onChangeDial = value => {
    const dialValue = Math.round(value);
    const activeSubType = angleMap[dialValue];
    changeOption(activeSubType);
  };

  const itemList = iconMap(activeSubType, theme);

  return (
    <DialContainer>
      {optionsOrder.map((subType, index) => {
        const item = itemList[subType];
        return (
          <IconWrapper
            key={index}
            style={{
              transform: item.transform,
            }}
          >
            <IconButton onClick={onClickButton(subType)} size="medium">
              {item.icon}
            </IconButton>
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

export default withTheme(Dial);
