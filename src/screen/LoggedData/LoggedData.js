import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Scrollbars } from 'react-custom-scrollbars';
import IconButton from '@material-ui/core/IconButton';
import CircularProgress from '@material-ui/core/CircularProgress';
import { Delete as DeleteIcon } from '@material-ui/icons';
import {
  OscilloscopeIcon,
  LogicAnalyserIcon,
  WaveGeneratorIcon,
  PowerSourceIcon,
  MultimeterIcon,
} from '../../components/Icons/PSLabIcons';
import {
  Container,
  Wrapper,
  CustomCard,
  Spacer,
  ButtonContainer,
  ContentWrapper,
  TextContainer,
  TitleWrapper,
  InfoContainer,
} from './LoggedData.styles.js';
const { remote } = window.require('electron');
const fs = remote.require('fs');
const os = remote.require('os');
const path = remote.require('path');
const chokidar = window.require('chokidar');

class LoggedData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      fileList: [],
    };
  }

  componentDidMount() {
    this.destDir = path.join(os.homedir(), 'Documents', 'PSLab');
    this.watcher = chokidar.watch(this.destDir);
    this.setState({
      loading: true,
    });

    this.listFiles('.csv');
    this.watcher.on('all', (event, path) => {
      this.listFiles('.csv');
    });
  }

  componentWillUnmount() {
    this.watcher.unwatch(this.destDir);
  }

  listFiles = extension => {
    fs.readdir(this.destDir, (err, files) => {
      const processedFiles = files
        .filter(files => {
          return path.extname(files).toLowerCase() === extension;
        })
        .map(file => {
          const filepath = path.join(this.destDir, file);
          return {
            name: file,
            filepath,
            metaData: this.getMetaData(filepath),
          };
        });
      this.setState({
        fileList: processedFiles,
        loading: false,
      });
    });
  };

  deleteFile = path => {
    fs.unlink(path, err => {
      if (err) {
        console.log(err);
      }
    });
  };

  getMetaData = path => {
    const content = fs.readFileSync(path, 'utf8');
    const data = content.split(/\r?\n/)[0].split(',');
    return {
      device: data[0],
      date: data[1],
      time: data[2],
    };
  };

  iconRenderer = device => {
    switch (device) {
      case 'Oscilloscope':
        return <OscilloscopeIcon color="red" size={'2em'} />;
      case 'LogicAnalyser':
        return <LogicAnalyserIcon color="red" size={'2em'} />;
      case 'WaveGenerator':
        return <WaveGeneratorIcon color="red" size={'2em'} />;
      case 'PowerSource':
        return <PowerSourceIcon color="red" size={'2em'} />;
      case 'Multimeter':
        return <MultimeterIcon color="red" size={'2em'} />;
      default:
        break;
    }
  };

  render() {
    const { loading, fileList } = this.state;
    const { history } = this.props;
    return (
      <Container>
        {loading ? (
          <CircularProgress />
        ) : (
          <Scrollbars autoHide autoHideTimeout={1000}>
            <Wrapper>
              {fileList.map((item, index) => (
                <CustomCard key={index}>
                  <ContentWrapper
                    onClick={() =>
                      history.push(`/${item.metaData.device.toLowerCase()}`)
                    }
                  >
                    <ButtonContainer>
                      {this.iconRenderer(item.metaData.device)}
                    </ButtonContainer>
                    <TextContainer>
                      <TitleWrapper>{item.metaData.device}</TitleWrapper>
                      <InfoContainer>
                        <div>{item.metaData.date}</div>
                        <div>{item.metaData.time}</div>
                      </InfoContainer>
                    </TextContainer>
                    <Spacer />
                    <ButtonContainer>
                      <IconButton
                        onClick={e => {
                          e.stopPropagation();
                          this.deleteFile(item.filepath);
                        }}
                        aria-label="Delete"
                        size="medium"
                      >
                        <DeleteIcon style={{ color: '#d32f2f' }} />
                      </IconButton>
                    </ButtonContainer>
                  </ContentWrapper>
                </CustomCard>
              ))}
            </Wrapper>
          </Scrollbars>
        )}
      </Container>
    );
  }
}

export default withRouter(LoggedData);
