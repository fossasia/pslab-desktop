const electron = require('electron');
const path = require('path');
const url = require('url');
const { ipcMain } = require('electron');
const loadBalancer = require('electron-load-balancer');

const { app } = electron;
const { BrowserWindow } = electron;
const nativeImage = electron.nativeImage;

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
      enableRemoteModule: true,
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
