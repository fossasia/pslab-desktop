import { createStore, combineReducers } from 'redux';
import { appReducer } from './reducers/app';
import { oscilloscopeReducer } from './reducers/oscilloscope';

const reducer = combineReducers({
  app: appReducer,
  oscilloscope: oscilloscopeReducer,
});

export const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
);
