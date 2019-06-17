import { createStore, combineReducers } from 'redux';
import { appReducer } from './reducers/app';

const reducer = combineReducers({
  app: appReducer,
});

export const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
);
