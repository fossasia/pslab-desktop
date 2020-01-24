const os = window.require('os');
const path = window.require('path');
const dataPath = path.join(os.homedir(), 'Documents', 'PSLab');

// Create save path if not existing

const initialState = {
  dataPath,
};

export const configReducer = (prevState = initialState, action) => {
  switch (action.type) {
    default:
      return initialState;
  }
};
