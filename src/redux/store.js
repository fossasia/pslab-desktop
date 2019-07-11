import { createStore, combineReducers } from 'redux';
import { appReducer } from './reducers/app';
import { configReducer } from './reducers/config';

const reducer = combineReducers({
  app: appReducer,
  config: configReducer,
});

export const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
);
