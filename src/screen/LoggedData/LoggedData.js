import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { withRouter } from 'react-router-dom';
import { Scrollbars } from 'react-custom-scrollbars';
import IconButton from '@material-ui/core/IconButton';
import {
  Delete as DeleteIcon,
  ScreenShare as ExportIcon,
} from '@material-ui/icons';
import {
  OscilloscopeIcon,
  LogicAnalyzerIcon,
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
  InstrumentWrapper,
  EmptyWrapper,
} from './LoggedData.styles.js';
import {
  fileNameTrimmer,
  extractFileName,
} from '../../utils/fileNameProcessor';
import { openSnackbar } from '../../redux/actions/app';
const { remote } = window.require('electron');
const fs = remote.require('fs');
const os = remote.require('os');
const path = remote.require('path');
const { dialog } = remote;
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
    if (!fs.existsSync(this.destDir)) {
      fs.mkdirSync(this.destDir);
    }
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

  openExportWindow(filePath) {
    const { openSnackbar } = this.props;
    const fileName = extractFileName(filePath);
    dialog.showOpenDialog(
      null,
      {
        title: 'Select export location',
        properties: ['openDirectory'],
      },
      dirPath => {
        dirPath &&
          fs.copyFile(filePath, `${dirPath}/${fileName}`, err => {
            if (err) {
              openSnackbar({ message: 'Export failed' });
            }
            openSnackbar({ message: 'Export successful' });
          });
      },
    );
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
      case 'LogicAnalyzer':
        return <LogicAnalyzerIcon color="red" size={'2em'} />;
      case 'WaveGenerator':
        return <WaveGeneratorIcon color="red" size={'2em'} />;
      case 'PowerSource':
        return <PowerSourceIcon color="red" size={'2em'} />;
      case 'Multimeter':
        return <MultimeterIcon color="red" size={'2em'} />;
      case 'RobotArm':
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
          <EmptyWrapper>
            <div>There are no data logs to display</div>
          </EmptyWrapper>
        ) : (
          <Scrollbars autoHide autoHideTimeout={1000}>
            <Wrapper>
              {fileList.length !== 0 &&
                fileList.map((item, index) => (
                  <CustomCard key={index}>
                    <ContentWrapper
                      onClick={() =>
                        history.push(
                          `/${item.metaData.device.toLowerCase()}/${item.name}`,
                        )
                      }
                    >
                      <ButtonContainer>
                        {this.iconRenderer(item.metaData.device)}
                      </ButtonContainer>
                      <TextContainer>
                        <TitleWrapper>
                          {fileNameTrimmer(item.name, 23)}
                        </TitleWrapper>
                        <InstrumentWrapper>
                          {item.metaData.device}
                        </InstrumentWrapper>
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
                          size="medium"
                        >
                          <DeleteIcon style={{ color: '#d32f2f' }} />
                        </IconButton>
                        <IconButton
                          size="medium"
                          onClick={e => {
                            e.stopPropagation();
                            this.openExportWindow(item.filepath);
                          }}
                        >
                          <ExportIcon style={{ color: '#d32f2f' }} />
                        </IconButton>
                      </ButtonContainer>
                    </ContentWrapper>
                  </CustomCard>
                ))}
              {fileList.length === 0 && (
                <EmptyWrapper>
                  <div>There are no data logs to display</div>
                </EmptyWrapper>
              )}
            </Wrapper>
          </Scrollbars>
        )}
      </Container>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(
    {
      openSnackbar,
    },
    dispatch,
  ),
});

export default withRouter(connect(null, mapDispatchToProps)(LoggedData));
