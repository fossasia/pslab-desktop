const electron = require('electron');
const path = require('path');
const url = require('url');
const { ipcMain } = require('electron');
const loadBalancer = require('electron-load-balancer');

const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow;

function createWindow() {
	const startUrl = process.env.DEV
		? 'http://localhost:3000'
		: url.format({
				pathname: path.join(__dirname, '/../build/index.html'),
				protocol: 'file:',
				slashes: true,
		  });

	mainWindow = new BrowserWindow({ width: 800, height: 600 });
	mainWindow.loadURL(startUrl);
	mainWindow.webContents.openDevTools();

	mainWindow.on('closed', function() {
		mainWindow = null;
	});
}

app.on('ready', createWindow);

app.on('window-all-closed', function() {
	if (process.platform !== 'darwin') {
		app.quit();
	}
});

app.on('activate', function() {
	if (mainWindow === null) {
		createWindow();
	}
});

/* ----------------------------------- Your code starts here ------------------------------------- */

loadBalancer.register(ipcMain, {
	linker: '/src/background_tasks/linker.html',
});

ipcMain.on('TO_RENDERER_DATA', (event, args) => {
	mainWindow.webContents.send('TO_RENDERER_DATA', args);
});

ipcMain.on('TO_RENDERER_STATUS', (event, args) => {
	mainWindow.webContents.send('TO_RENDERER_STATUS', args);
});

ipcMain.on('DEBUG', (event, args) => {
	mainWindow.webContents.send('DEBUG', args);
});
