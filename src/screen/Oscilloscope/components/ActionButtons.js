import React from 'react';
import { Button, Icon } from 'antd';
import { ButtonWrapper } from './ActionButtons.styles';

const ActionButtons = props => {
	return (
		<ButtonWrapper>
			<Button block size="large">
				<Icon type="play-circle" />
			</Button>
			<Button block size="large">
				<Icon type="deployment-unit" />
			</Button>
		</ButtonWrapper>
	);
};

export default ActionButtons;
