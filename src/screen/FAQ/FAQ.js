import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import MuiExpansionPanel from '@material-ui/core/ExpansionPanel';
import MuiExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import MuiExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import { Container, Wrapper, Link } from './FAQ.styles';

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

  const openWindow = url => () => {
    window.open(url, '_blank', 'height=650,width=1000,frame=true,show=true');
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
              A: Connect the PSLab device to your computer using a USB adapter
              and micro usb cable. Start the application and click on an
              instrument you like to try out. The guide to use each instrument
              is available online.
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
              A: The guide for the schematic are available online.
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
              A: Right now, we don't having an option to make and save custom
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

        <ExpansionPanel
          square
          expanded={expanded === 'panel6'}
          onChange={handleChange('panel6')}
        >
          <ExpansionPanelSummary
            aria-controls="panel6d-content"
            id="panel6d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: What is Pocket Science Lab? What can I do with it?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: Pocket Science Lab (PSLab) is a small USB powered hardware
              board that can be used for measurements and experiments. It works
              as an extension for Android phones or PCs. PSLab comes with a
              built-in Oscilloscope, Multimeter, Wave Generator, Logic Analyzer,
              Power Source, and many more instruments. It can also be used as a
              robotics control app. And, we are constantly adding more digital
              instruments. PSLab is many devices in one. Simply connect two
              wires to the relevant pins (description is on the back of the
              PSLab board) and start measuring. You can use our Open Source
              Android or desktop app to view and collect the data. You can also
              plug in hundreds of compatible I²C standard sensors to the PSLab
              pin slots. It works without the need for programming. So, what
              experiments you do is just limited to your imagination!
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel7'}
          onChange={handleChange('panel7')}
        >
          <ExpansionPanelSummary
            aria-controls="panel7d-content"
            id="panel7d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Where can I buy a Pocket Science Lab?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A
              {`: There is an overview page for shops where you can buy a Pocket
              Science Lab device in different regions on the `}
              <Link
                onClick={openWindow(
                  'https://github.com/fossasia/pslab-desktop/tree/install',
                )}
              >
                website at https://pslab.io/shop/.
              </Link>
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel8'}
          onChange={handleChange('panel8')}
        >
          <ExpansionPanelSummary
            aria-controls="panel8d-content"
            id="panel8d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Where can I download the desktop app for Pocket Science Lab for
              Windows, Linux and Mac?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {
                'A: We are developing a desktop app for Windows, Linux and Mac in'
              }
              <Link
                onClick={openWindow(
                  'https://github.com/fossasia/pslab-desktop/tree/install',
                )}
              >
                our desktop Git repository. You can find it in the install
                branch of the project here
              </Link>
              {`. The app is still under development. We are
              using technologies like Electron and Python, that work on all
              platforms. However, to make the final installer work everywhere
              requires some tweaks and improvements here and there. So, please
              expect some glitches. You can use the tracker in the repository to
              submit issues, bugs and feature requests.`}
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel9'}
          onChange={handleChange('panel9')}
        >
          <ExpansionPanelSummary
            aria-controls="panel9d-content"
            id="panel9d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: How can I connect to the device? What kind of USB cable do I
              need? What is an OTG USB cable?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {'A: To connect to the device you need an OTG USB cable '}
              <Link
                onClick={openWindow(
                  'https://en.wikipedia.org/wiki/USB_On-The-Go',
                )}
              >
                (OTG = On the go)
              </Link>
              {` which is a USB cable that allows connected devices to
              switch back and forth between the roles of host and device. USB
              cables that are not OTG compatible will NOT work.`}
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel10'}
          onChange={handleChange('panel10')}
        >
          <ExpansionPanelSummary
            aria-controls="panel10d-content"
            id="panel10d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: I found a bug in one of your apps or hardware. What to do?
              Where should I report it?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {`A: We have issue trackers in all our projects. They are currently
              hosted on GitHub. In order to submit a bug or feature request you
              need to login to the service. `}
              <Link
                onClick={openWindow(
                  'https://github.com/fossasia?utf8=%E2%9C%93&q=pslab',
                )}
              >
                A list of our PSLab repositories is here
              </Link>
              {' (scroll down a bit, when you access this page).'}
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel11'}
          onChange={handleChange('panel11')}
        >
          <ExpansionPanelSummary
            aria-controls="panel11d-content"
            id="panel11d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Can I record or save data in the apps and export or import it?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: Yes, we have implemented a record and play function or a way to
              save and open configurations in the instruments on the Android and
              desktop app. Data you record can be imported into the apps and
              viewed. This feature is still under heavy development, but works
              well in most places. You can find it in the top bar of the apps.
              There are buttons to record, play, save and open data.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel12'}
          onChange={handleChange('panel12')}
        >
          <ExpansionPanelSummary
            aria-controls="panel12d-content"
            id="panel12d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Which external sensors can I use with a PSLab device and the
              apps? Which ones are compatible?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {'A: In our apps we use the industry standard I²C '}(
              <Link
                onClick={openWindow('https://en.wikipedia.org/wiki/I%C2%B2C')}
              >
                Wikipedia
              </Link>
              ).
              {` You
              can get the data from sensors that are connected to the device
              through the USB port using an OTG USB cable (OTG = On the go)
              which is a USB cable that allows connected devices to switch back
              and forth between the roles of host and device. For the transfer
              we use UART (universal asynchronous receiver-transmitter,`}
              <Link
                onClick={openWindow(
                  'https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter',
                )}
              >
                Wikipedia)
              </Link>
              {`. Many sensors can be used with specific instruments,
              e.g. Barometer, Thermometer, Gyroscope etc. You can access the
              configuration for sensors in the instrument settings on the top
              right burger menu of each instrument. All sensors using the I²C
              standard are compatible with the device. There are connection pins
              for analogue and digital sensors. You find the description of the
              pins on the back of the device. Even if there is no specific
              instrument in one of our apps yet, you can still view and store
              the raw data using the Oscilloscope instrument component. There is`}
              <Link onClick={openWindow('https://pslab.io/sensors/')}>
                a page with a list of recommended sensors on the website
              </Link>
              .
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel13'}
          onChange={handleChange('panel13')}
        >
          <ExpansionPanelSummary
            aria-controls="panel13d-content"
            id="panel13d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: How can I use the Pocket Science Lab as an independent data
              logger without the phone or desktop connected?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              A: We have already implemented this functionality, however it is
              still in prototype stage. You can generate a config file in the
              Android app ( feature not yet implemented in desktop app ) and
              transfer it to the PSLab device (you might have to update the
              firmware that you find on our Github org). You can power the PSLab
              device with an USB battery and it can collect data independently
              of the app. Once you connect the app you can download the data
              collected. Future versions of the device will come with a SD card
              to store the data locally as well. At the moment there are still
              limits to using this feature, but we are continuously working on
              it{' '}
              <span role="img" aria-label="smiley">
                🙂
              </span>
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel14'}
          onChange={handleChange('panel14')}
        >
          <ExpansionPanelSummary
            aria-controls="panel14d-content"
            id="panel14d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: It is cool, that PSLab is Open Hardware! Where can I find the
              schematics and parts list of Pocket Science Lab?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {'The PSLab hardware is developed using '}
              <Link onClick={openWindow('http://www.kicad-pcb.org/')}>
                KiCad
              </Link>
              {`. The software can
              generate all kinds of formats and components lists. You can find
              the schematics and source files in the `}
              <Link
                onClick={openWindow(
                  'https://github.com/fossasia/pslab-hardware',
                )}
              >
                hardware Git repository here
              </Link>
              .
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel15'}
          onChange={handleChange('panel15')}
        >
          <ExpansionPanelSummary
            aria-controls="panel15d-content"
            id="panel15d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: Who develops PSLab? When did you start it? What is the story
              behind it?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {'A: PSLab is developed with a community at '}
              <Link onClick={openWindow('https://fossasia.org/')}>
                FOSSASIA
              </Link>
              {`. There are over
              100 developers who have contributed to the project across
              different repositories. The project was started after Praveen
              Kumar, a physics teacher from India, introduced the idea of an
              open physics lab device inspired by the ExpEYES project at the
              FOSSASIA Summit in Cambodia 2014. He helped to get the project
              moving forward and worked with early contributors on the software
              components. The Open Hardware board was released in 2017 as part
              of a GSoC project by Jithin B P who used the ExpEYES boards he
              developed earlier as a basis to create the first version of PSLab.
              In the following years hardware components were updated, the size
              and design was adjusted resulting in much lower production costs
              and many features were added in the firmware. An Android app was
              developed from scratch and most of the desktop app re-implemented
              with a new cross-platform Electron frontend. `}
              <Link onClick={openWindow('https://twitter.com/Cloudypadmal')}>
                Padmal M
              </Link>
              {` from Sri
              Lanka is leading the tech team since 2018 and defines the roadmap
              together with `}
              <Link onClick={openWindow('https://twitter.com/mariobehling')}>
                Mario Behling
              </Link>
              {`, core developers and contributors from
              the wider community. Since 2019 FOSSASIA produces batches of the
              boards in large quantities. It is our goal to set an example as an
              Open Hardware project, to make it commercially sustainable and
              inspire others to create Open Hardware and Free and Open Source
              software.`}
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel
          square
          expanded={expanded === 'panel16'}
          onChange={handleChange('panel16')}
        >
          <ExpansionPanelSummary
            aria-controls="panel16d-content"
            id="panel16d-header"
          >
            <Typography style={{ color: '#d32f2f' }}>
              Q: I found a mistake on the website, where can I submit the issue?
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {'A: We use issue trackers for most of our work. You can submit '}
              <Link
                onClick={openWindow(
                  'https://github.com/fossasia/pslab.io/issues',
                )}
              >
                issues you find regarding the website on our issue tracker here
              </Link>
              {'.'}
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
      </Wrapper>
    </Container>
  );
};
export default FAQ;
