import React from 'react';
import { Container, Wrapper } from './AboutUs.styles';
import AppIcon from '../../resources/app_icon.png';
import { BugReport as BugIcon } from '@material-ui/icons';
import {
  Typography,
  Divider,
  ListItem,
  ListItemIcon,
  ListItemText,
} from '@material-ui/core';
import TwitterIcon from '../../resources/t.png';
import GithubIcon from '../../resources/git.png';
import FacebookIcon from '../../resources/fb.png';
import YoutubeIcon from '../../resources/yt.png';
import { Link as LinkIcon, Email as MailIcon } from '@material-ui/icons';

const AboutUs = () => {
  return (
    <Container>
      <Wrapper>
        <img
          alt=""
          src={AppIcon}
          style={{ height: '20em', width: '20em', margin: '0px 16px' }}
        />
        <Typography
          style={{
            width: 'calc(100% - 96px)',
            fontSize: '1.4em',
            textAlign: 'center',
            margin: '16px 48px 16px 48px',
          }}
        >
          The goal of PSLab is to create an Open Source hardware device (open on
          all layers) that can be used for experiments by teachers, students and
          citizen scientists. Our tiny pocket lab provides an array of sensors
          for doing science and engineering experiments. It provides functions
          of numerous measurement devices including an oscilloscope, a waveform
          generator, a frequecy counter, a programmable voltabe, current source
          and as a data logger.
        </Typography>
        <Divider
          style={{
            width: '100%',
          }}
        />
        <Typography
          style={{
            width: 'calc(100% - 16px)',
            fontSize: '1.6em',
            margin: '8px 0px 0px 16px',
          }}
        >
          Connect with us
        </Typography>
        <ListItem
          button
          style={{
            margin: '8px 0px 0px 0px',
          }}
          onClick={() => {
            window.open(
              'mailto:pslab-fossasia@googlegroups.com',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <MailIcon style={{ height: '1.6em', width: '1.6em' }} />
          </ListItemIcon>
          <ListItemText primary="Contact us" />
        </ListItem>
        <Divider
          style={{
            width: '100%',
          }}
        />
        <ListItem
          button
          onClick={() => {
            window.open(
              'https://pslab.io/',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <LinkIcon style={{ height: '1.6em', width: '1.6em' }} />
          </ListItemIcon>
          <ListItemText primary="Visit our website" />
        </ListItem>
        <Divider
          style={{
            width: '100%',
          }}
        />
        <ListItem
          button
          onClick={() => {
            window.open(
              'https://github.com/fossasia/pslab-desktop',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <img
              src={GithubIcon}
              style={{ height: '3em', width: '3em' }}
              alt=""
            />
          </ListItemIcon>
          <ListItemText primary="Fork us on Github" />
        </ListItem>
        <Divider
          style={{
            width: '100%',
          }}
        />
        <ListItem
          button
          onClick={() => {
            window.open(
              'https://www.facebook.com/pslabio',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <img
              src={FacebookIcon}
              style={{ height: '3em', width: '3em' }}
              alt=""
            />
          </ListItemIcon>
          <ListItemText primary="Like us on Facebook" />
        </ListItem>
        <Divider
          style={{
            width: '100%',
          }}
        />
        <ListItem
          button
          onClick={() => {
            window.open(
              'https://twitter.com/pslabio',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <img
              src={TwitterIcon}
              style={{ height: '3em', width: '3em' }}
              alt=""
            />
          </ListItemIcon>
          <ListItemText primary="Follow us on Twitter" />
        </ListItem>
        <Divider
          style={{
            width: '100%',
          }}
        />
        <ListItem
          button
          onClick={() => {
            window.open(
              'https://www.youtube.com/channel/UCQprMsG-raCIMlBudm20iLQ',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <img
              src={YoutubeIcon}
              style={{ height: '3em', width: '3em' }}
              alt=""
            />
          </ListItemIcon>
          <ListItemText primary="Watch us on Youtube" />
        </ListItem>
        <ListItem
          button
          onClick={() => {
            window.open(
              'https://docs.google.com/forms/d/e/1FAIpQLSfn2MAk_4TzJ07iu93KNU8g2Ac3UHm2aKww1qJVsduSbsI4Wg/viewform ',
              '_blank',
              'height=650,width=1000,frame=true,show=true',
            );
          }}
        >
          <ListItemIcon>
            <BugIcon style={{ fontSize: '36px' }} />
          </ListItemIcon>
          <ListItemText primary="Feedback & Bugs" />
        </ListItem>
      </Wrapper>
    </Container>
  );
};

export default AboutUs;
