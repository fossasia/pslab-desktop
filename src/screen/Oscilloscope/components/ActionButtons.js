import React from 'react';
import { Button, Icon } from 'antd';
import { ButtonWrapper } from './ActionButtons.styles';

const ActionButtons = ({ isReading, onToggleRead }) => {
	return (
		<ButtonWrapper>
			<Button onClick={onToggleRead} block size="large">
				{isReading ? <Icon type="loading" /> : <Icon type="caret-right" />}
			</Button>
			<Button block size="large">
				<Icon type="deployment-unit" />
			</Button>
		</ButtonWrapper>
	);
};

export default ActionButtons;
