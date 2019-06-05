const electron = require('electron');
const path = require('path');
const url = require('url');
const { ipcMain } = require('electron');
const loadBalancer = require('electron-load-balancer');

const { app } = electron;
const { BrowserWindow } = electron;
const nativeImage = electron.nativeImage;

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
  mainWindow = new BrowserWindow({ show: false, icon });
  mainWindow.maximize();
  mainWindow.show();

  mainWindow.loadURL(startUrl);
  process.env.DEV && mainWindow.webContents.openDevTools();

  mainWindow.on('closed', function() {
    loadBalancer.stopAllBackgroundProcess();
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

/* ----------------------------------- Your code starts here ------------------------------------- */

loadBalancer.register(ipcMain, {
  linker: '/background_tasks/linker.html',
});

ipcMain.on('TO_RENDERER_DATA', (event, args) => {
  mainWindow.webContents.send('TO_RENDERER_DATA', args);
});

ipcMain.on('TO_RENDERER_CONFIG', (event, args) => {
  mainWindow.webContents.send('TO_RENDERER_CONFIG', args);
});

ipcMain.on('TO_RENDERER_STATUS', (event, args) => {
  mainWindow.webContents.send('TO_RENDERER_STATUS', args);
});

ipcMain.on('DEBUG', (event, args) => {
  mainWindow.webContents.send('DEBUG', args);
});
