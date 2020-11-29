const { remote } = require('electron');
const path = require('path');

const scriptDir = 'scripts';

/**
 * Get the path to the request Python script, specified by its name.
 * In dev mode, the path is just relative to the files in `background_tasks`.
 * For distribution, we bundle everything into an asar archive except for the
 * Python scripts. Otherwise, the Python interpreter cannot locate them.
 */
const getScriptPath = scriptName => {
  const appPath = remote.app.getAppPath();
  if (process.env.DEV) {
    return path.join(appPath, scriptDir, scriptName);
  }
  return path
    .join(appPath, scriptDir, scriptName)
    .replace('app.asar', 'app.asar.unpacked');
};

module.exports = {
  getScriptPath,
};
