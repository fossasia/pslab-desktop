import React from 'react';
import { SettingsContainer, SettingsWrapper } from './Settings.styles';
import { Button, Switch, Card } from 'antd';

const Settings = props => {
	return (
		<SettingsContainer>
			<SettingsWrapper>
				<Card style={{ width: '100%', heigh: '200px' }}>Setings 1</Card>
			</SettingsWrapper>
			<SettingsWrapper>
				<Card style={{ width: '100%', heigh: '200px' }}>Setings 1</Card>
			</SettingsWrapper>
			<SettingsWrapper>
				<Card style={{ width: '100%', heigh: '200px' }}>Setings 1</Card>
			</SettingsWrapper>
		</SettingsContainer>
	);
};

export default Settings;
