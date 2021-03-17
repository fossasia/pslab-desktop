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
import { fileNameTrimmer } from '../../utils/fileNameProcessor';
import { openSnackbar } from '../../redux/actions/app';

const electron = window.require('electron');
const { ipcRenderer } = electron;
const chokidar = window.require('chokidar');

class LoggedData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      fileList: [],
    };
  }

  componentDidMount = async () => {
    const { dataPath } = this.props;
    await ipcRenderer.invoke('MAKE_DIRECTORY', dataPath);
    this.watcher = chokidar.watch(dataPath);
    this.setState({
      loading: true,
    });
    this.listFiles('.csv');
    this.watcher.on('all', (event, path) => {
      this.listFiles('.csv');
    });
  };

  componentWillUnmount() {
    this.watcher.unwatch(this.destDir);
  }

  openExportWindow = async filePath => {
    const { openSnackbar } = this.props;
    ipcRenderer.invoke('OPEN_EXPORT_WINDOW', filePath).then(message => {
      if (message) {
        openSnackbar({ message: message });
      }
    });
  };

  listFiles = extension => {
    const { dataPath } = this.props;
    ipcRenderer
      .invoke('LIST_FILES', dataPath, extension)
      .then(processedFiles => {
        this.setState({
          fileList: processedFiles,
          loading: false,
        });
      });
  };

  deleteFile = path => {
    ipcRenderer.invoke('DELETE_FILE', path);
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
