import React from 'react';
import { IconButton } from '@material-ui/core';
import { DialContainer, IconWrapper, DialWrapper } from './Dial.styles';
import { withTheme } from 'styled-components';
import CustomKnob from '../../../components/CustomKnob';
import { iconMap, optionsOrder, angleMap } from './SettingOptions';

const Dial = ({
  value,
  onClickButton,
  changeDialValue,
  changeOption,
  activeSubType,
  theme,
}) => {
  const onChangeDial = value => {
    let dialValue = Math.round(value);
    Object.keys(angleMap).map(angle => {
      const compAngle = parseInt(angle, 10);
      if (compAngle - 5 <= dialValue && dialValue < compAngle + 5) {
        dialValue = compAngle;
      }
      return null;
    });
    const activeSubType = angleMap[dialValue];
    if (activeSubType) {
      changeOption(activeSubType);
    } else {
      changeDialValue(dialValue);
    }
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
        <CustomKnob
          onChangeDial={onChangeDial}
          value={value}
          radius={20}
          min={0}
          max={360}
          step={32.7}
        />
      </DialWrapper>
    </DialContainer>
  );
};

export default withTheme(Dial);
