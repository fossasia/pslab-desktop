const electron = require('electron');
const path = require('path');
const url = require('url');
const fs = require('fs');
const { ipcMain } = require('electron');
const loadBalancer = require('electron-load-balancer');

const { app } = electron;
const { BrowserWindow, dialog } = electron;
const nativeImage = electron.nativeImage;

const scriptDir = 'scripts';

/**
 * Get the path to the requested Python script, specified by its name.
 * In dev mode, the path is just relative to the files in `background_tasks`.
 * For distribution, we bundle everything into an asar archive except for the
 * Python scripts. Otherwise, the Python interpreter cannot locate them.
 */
const getScriptPath = scriptName => {
  const appPath = app.getAppPath();
  if (process.env.DEV) {
    return path.join(appPath, scriptDir, scriptName);
  }
  return path
    .join(appPath, scriptDir, scriptName)
    .replace('app.asar', 'app.asar.unpacked');
};

if (process.env.DEV) {
  const {
    default: installExtension,
    REDUX_DEVTOOLS,
    REACT_DEVELOPER_TOOLS,
  } = require('electron-devtools-installer');

  app.whenReady().then(() => {
    installExtension(REDUX_DEVTOOLS).then(name =>
      console.log(`Added Extension:  ${name}`),
    );
    installExtension(REACT_DEVELOPER_TOOLS).then(name =>
      console.log(`Added Extension:  ${name}`),
    );
  });
}

const icon = nativeImage.createFromPath(path.join(__dirname, 'app_icon.png'));
let mainWindow;

function createWindow() {
  const startUrl = process.env.DEV
    ? 'http://localhost:3000'
    : url.format({
        pathname: path.join(__dirname, '/../build/index.html'),
        protocol: 'file:',
        slashes: true,
      });
  mainWindow = new BrowserWindow({
    show: false,
    icon,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: false,
    },
    minWidth: 500,
    minHeight: 300,
  });
  mainWindow.maximize();
  mainWindow.show();

  mainWindow.loadURL(startUrl);
  process.env.DEV && mainWindow.webContents.openDevTools();

  mainWindow.on('closed', function() {
    loadBalancer.stopAll();
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

/* ----------------------------------- Custom code starts here ------------------------------------- */

loadBalancer.register(
  ipcMain,
  {
    linker: '/background_tasks/linker.html',
    playback: '/background_tasks/playback.html',
  },
  // Set to true to unhide the window, useful for IPC debugging
  { debug: false },
);

ipcMain.on('OSC_VOLTAGE_DATA', (event, args) => {
  mainWindow.webContents.send('OSC_VOLTAGE_DATA', args);
});

ipcMain.on('OSC_XY_PLOT_DATA', (event, args) => {
  mainWindow.webContents.send('OSC_XY_PLOT_DATA', args);
});

ipcMain.on('OSC_FFT_DATA', (event, args) => {
  mainWindow.webContents.send('OSC_FFT_DATA', args);
});

ipcMain.on('OSC_FIT_DATA', (event, args) => {
  mainWindow.webContents.send('OSC_FIT_DATA', args);
});

ipcMain.on('LA_DATA', (event, args) => {
  mainWindow.webContents.send('LA_DATA', args);
});

ipcMain.on('MUL_MET_DATA', (event, args) => {
  mainWindow.webContents.send('MUL_MET_DATA', args);
});

ipcMain.on('PWR_SRC_CONFIG', (event, args) => {
  mainWindow.webContents.send('PWR_SRC_CONFIG', args);
});

ipcMain.on('OSC_CONFIG', (event, args) => {
  mainWindow.webContents.send('OSC_CONFIG', args);
});

ipcMain.on('LA_CONFIG', (event, args) => {
  mainWindow.webContents.send('LA_CONFIG', args);
});

ipcMain.on('MUL_MET_CONFIG', (event, args) => {
  mainWindow.webContents.send('MUL_MET_CONFIG', args);
});

ipcMain.on('WAV_GEN_CONFIG', (event, args) => {
  mainWindow.webContents.send('WAV_GEN_CONFIG', args);
});

ipcMain.on('CONNECTION_STATUS', (event, args) => {
  mainWindow.webContents.send('CONNECTION_STATUS', args);
  mainWindow.webContents.send('CONNECTION_STATUS_MUL_MET', args);
  mainWindow.webContents.send('CONNECTION_STATUS_OSC', args);
});

ipcMain.on('DATA_WRITING_STATUS', (event, args) => {
  mainWindow.webContents.send('DATA_WRITING_STATUS', args);
});

ipcMain.on('FETCH_ROB_ARM', (event, args) => {
  mainWindow.webContents.send('FETCH_ROB_ARM', args);
});

ipcMain.on('FETCH_LA', (event, args) => {
  mainWindow.webContents.send('FETCH_LA', args);
});

ipcMain.on('SENSORS_SCAN', (event, args) => {
  mainWindow.webContents.send('SENSORS_SCAN', args);
});

ipcMain.handle('GET_SCRIPT_PATH', (event, args) => {
  return getScriptPath(args);
});

ipcMain.handle('OPEN_IMPORT_WINDOW', async (event, dataPath) => {
  return dialog
    .showOpenDialog(null, {
      title: 'Select file(s) to import',
      filters: [{ name: 'Data File', extensions: ['csv'] }],
      properties: ['openFile', 'multiSelections'],
    })
    .then(result => {
      if (result.filePaths) {
        var message = 'Import successful';
        result.filePaths.forEach(filePath => {
          const fileName = extractFileName(filePath);
          fs.copyFile(filePath, `${dataPath}/${fileName}`, err => {
            if (err) {
              console.log(err);
              message = 'Import failed';
            }
          });
        });
      }
      return message;
    })
    .catch(err => {
      console.log(err);
    });
});

ipcMain.handle('OPEN_EXPORT_WINDOW', async (event, filePath) => {
  return dialog
    .showOpenDialog(null, {
      title: 'Select export location',
      properties: ['openDirectory'],
    })
    .then(result => {
      const dirPath = result.filePaths[0];
      if (dirPath) {
        var message = 'Export successful';
        const fileName = filePath.replace(/.*\//, '');
        fs.copyFile(filePath, `${dirPath}/${fileName}`, err => {
          if (err) {
            console.log(err);
            message = 'Export failed';
          }
        });
        return message;
      }
    })
    .catch(err => {
      console.log(err);
    });
});

ipcMain.handle('MAKE_DIRECTORY', (event, dirPath) => {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
});

ipcMain.handle('DELETE_FILE', (event, path) => {
  fs.unlink(path, err => {
    if (err) {
      console.log(err);
    }
  });
});

ipcMain.handle('LIST_FILES', (event, dirPath, extension) => {
  const processedFiles = fs
    .readdirSync(dirPath)
    .filter(files => {
      return path.extname(files).toLowerCase() === extension;
    })
    .map(file => {
      const filepath = path.join(dirPath, file);
      return {
        name: file,
        filepath,
        metaData: getMetaData(filepath),
      };
    });
  return processedFiles;
});

getMetaData = path => {
  const content = fs.readFileSync(path, 'utf8');
  const data = content.split(/\r?\n/)[0].split(',');
  return {
    device: data[0],
    date: data[1],
    time: data[2],
  };
};
