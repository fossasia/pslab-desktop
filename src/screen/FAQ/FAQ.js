import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import MuiExpansionPanel from '@material-ui/core/ExpansionPanel';
import MuiExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import MuiExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import { Container, Wrapper } from './FAQ.styles';

const ExpansionPanel = withStyles({
  root: {
    border: '1px solid rgba(0, 0, 0, .125)',
    boxShadow: 'none',
    '&:not(:last-child)': {
      borderBottom: 0,
    },
    '&:before': {
      display: 'none',
    },
    '&$expanded': {
      margin: 'auto',
    },
  },
  expanded: {},
})(MuiExpansionPanel);

const ExpansionPanelSummary = withStyles({
  root: {
    backgroundColor: 'rgba(0, 0, 0, .03)',
    borderBottom: '1px solid rgba(0, 0, 0, .125)',
    marginBottom: -1,
    minHeight: 56,
    '&$expanded': {
      minHeight: 56,
    },
  },
  content: {
    '&$expanded': {
      margin: '12px 0',
    },
  },
  expanded: {},
})(MuiExpansionPanelSummary);

const ExpansionPanelDetails = withStyles(theme => ({
  root: {
    padding: '16px',
  },
}))(MuiExpansionPanelDetails);

const FAQ = () => {
  const [expanded, setExpanded] = React.useState('panel1');

  const handleChange = panel => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

  return (
    <Container>
      <Wrapper>
        <ExpansionPanel
          square
          expanded={expanded === 'panel1'}
          onChange={handleChange('panel1')}
        >
          <ExpansionPanelSummary
            aria-controls="panel1d-content"
            id="panel1d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: How can I use this application?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: Each instrument includes a bottomsheet guide which gets open
              when you slide up from the bottom of your screen. It includes all
              the necessary details to connect the device along a brief guide to
              use it.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <ExpansionPanel
          square
          expanded={expanded === 'panel2'}
          onChange={handleChange('panel2')}
        >
          <ExpansionPanelSummary
            aria-controls="panel2d-content"
            id="panel2d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: What are the experiments I can perform?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: The goal of PSLab is to create an Open Source hardware device
              (open on all layers) that can be used for experiments by teachers,
              students and citizen scientists. Our tiny pocket science lab
              provides an array of sensors for doing science and engineering
              experiments. It provides functions of numerous measurement devices
              including an oscilloscope, a waveform generator, a frequecy
              counter, a programmable voltage, current source and as a data
              logger.Hence you can perform all kind of experiments using these
              devices.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <ExpansionPanel
          square
          expanded={expanded === 'panel3'}
          onChange={handleChange('panel3')}
        >
          <ExpansionPanelSummary
            aria-controls="panel3d-content"
            id="panel3d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Where can I find the schematic for connections of the
              instruments?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: The bottomsheet guide implemented in each instrument has all
              the schematics for the connection of the device
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <ExpansionPanel
          square
          expanded={expanded === 'panel4'}
          onChange={handleChange('panel4')}
        >
          <ExpansionPanelSummary
            aria-controls="panel4d-content"
            id="panel4d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: How can I design my own experiment and save it?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: Right now, we are not having an option to make and save custom
              experiments. But we will implement it soon.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <ExpansionPanel
          square
          expanded={expanded === 'panel5'}
          onChange={handleChange('panel5')}
        >
          <ExpansionPanelSummary
            aria-controls="panel5d-content"
            id="panel5d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Can I submit a change request for a particular instrument? If
              so, how?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: You can submit your reviews, feature requests and feedback
              through our Feedback and Issues page.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
      </Wrapper>
    </Container>
  );
};

export default FAQ;
