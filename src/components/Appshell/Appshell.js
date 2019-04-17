import React from 'react';
import { Link, withRouter } from 'react-router-dom';
import {
	AppshellContainer,
	ChildrenContainer,
	NavigationContainer,
	TopNavigationWrapper,
	BottomNavigationWrapper,
	Spacer,
	NavigationTab,
	AppIconWrapper
} from './Appshell.styles';
import AppIcon from '../../resources/app_icon.svg';
import { MdGridOn, MdSettings, MdTimeline, MdExposure } from 'react-icons/md';

const topNavigationItems = [
	{
		name: 'Oscilloscope',
		redirectPath: '/oscilloscope',
		icon: <MdGridOn size={'2.2em'} />,
	},
	{
		name: 'Logica Analyser',
		redirectPath: '/logicanalyser',
		icon: <MdTimeline size={'2.2em'} />,
	},
	{
		name: 'Power Source',
		redirectPath: '/powersource',
		icon: <MdExposure size={'2.2em'} />,
	}
];

const Appshell = props => {
	const { children, location } = props;

	return (
		<AppshellContainer>
			<NavigationContainer>
				<AppIconWrapper>
					<img style={
						{
							height: '3em',
							width: 'auto'
						}
					} alt="App Icon" src={AppIcon}/>
				</AppIconWrapper>
				<TopNavigationWrapper>
					{topNavigationItems.map((item, index) => {
						return (
							<Link key={index} to={item.redirectPath}>
								<NavigationTab selected={item.redirectPath === location.pathname}>
									{item.icon}
								</NavigationTab>
							</Link>
						);
					})}
				</TopNavigationWrapper>
				<Spacer />
				<BottomNavigationWrapper>
					<Link to="/settings">
						<NavigationTab>
							<MdSettings size={'2.2em'} />
						</NavigationTab>
					</Link>
				</BottomNavigationWrapper>
			</NavigationContainer>
			<ChildrenContainer>{children}</ChildrenContainer>
		</AppshellContainer>
	);
};

export default withRouter(Appshell);
