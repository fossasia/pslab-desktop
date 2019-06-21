import React from 'react';
import HomeLayout from '../../components/HomeLayout';
import Tabs from './components/Tabs';

const Home = props => {
  return <HomeLayout tabs={<Tabs />} />;
};

export default Home;
