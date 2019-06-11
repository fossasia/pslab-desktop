import { createStore, combineReducers } from 'redux';
import { appReducer } from './reducers/app';

const reducer = combineReducers({
  app: appReducer,
});

export const store = createStore(reducer);
