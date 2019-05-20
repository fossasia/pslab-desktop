import React from 'react';
import { DialContainer, IconWrapper, DialWrapper } from './Dial.styles';
import { withTheme } from 'styled-components';
import CustomCircularInput from '../../../components/CustomCircularInput';
import { options, optionsOrder } from './SettingOptions';

const Dial = ({ value, onClickButton, activeSubType, theme }) => {
  const onChangeDial = value => {
    const dialValue = Math.round(value);
    let activeSubType = null;
    switch (dialValue) {
      case 0:
        activeSubType = 'CH1';
        break;
      case 360:
        activeSubType = 'CH1';
        break;
      case 33:
        activeSubType = 'CAPACITOR';
        break;
      case 65:
        activeSubType = 'RESISTOR';
        break;
      case 98:
        activeSubType = 'ID4';
        break;
      case 131:
        activeSubType = 'ID3';
        break;
      case 164:
        activeSubType = 'ID2';
        break;
      case 196:
        activeSubType = 'ID1';
        break;
      case 229:
        activeSubType = 'AN8';
        break;
      case 262:
        activeSubType = 'CAP';
        break;
      case 294:
        activeSubType = 'CH3';
        break;
      case 327:
        activeSubType = 'CH2';
        break;
      default:
        break;
    }
    onClickButton(
      activeSubType,
      options(activeSubType, onClickButton, theme)[activeSubType].unit,
      dialValue,
    )();
  };

  return (
    <DialContainer>
      {optionsOrder.map((subType, index) => {
        const item = options(activeSubType, onClickButton, theme)[subType];
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

export default withTheme(Dial);
