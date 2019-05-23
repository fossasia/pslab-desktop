import { createMuiTheme } from '@material-ui/core/styles';

const theme = createMuiTheme({
  pallet: {
    common: {
      black: '#000',
      white: '#fff',
    },
    background: {
      paper: 'rgba(255, 255, 255, 1)',
      default: 'rgba(181, 181, 181, 0.2)',
    },
    primary: {
      light: 'rgba(142, 155, 224, 1)',
      main: 'rgba(107, 2, 246, 1)',
      dark: '#303f9f',
      contrastText: 'rgba(255, 255, 255, 1)',
    },
    secondary: {
      light: 'rgba(220, 90, 50, 1)',
      main: 'rgba(255, 5, 5, 1)',
      dark: 'rgba(196, 74, 103, 1)',
      contrastText: '#fff',
    },
    error: {
      light: '#e57373',
      main: '#f44336',
      dark: '#d32f2f',
      contrastText: '#fff',
    },
    text: {
      primary: 'rgba(0, 0, 0, 0.87)',
      secondary: 'rgba(0, 0, 0, 0.54)',
      disabled: 'rgba(0, 0, 0, 0.38)',
      hint: 'rgba(0, 0, 0, 0.38)',
    },
    linkColor: '#1890ff',
    headingColor: 'rgba(0, 0, 0, .85)',
    disabledColor: 'rgba(0, 0, 0, .25)',
    gradient:
      'rgb(220, 90, 50) linear-gradient(-90deg, rgb(220, 90, 50), rgb(196, 74, 103)) repeat scroll 0% 0%',
    iconBackground: '#ffffff',
    navigationBackground: '#bdbdbd',
    ch1Color: '#ff9800',
    ch2Color: '#03a9f4',
    ch3Color: '#4caf50',
    micColor: '#5e35b1',
    s1Color: '#ff9800',
    s2Color: '#03a9f4',
    sqr1Color: '#4caf50',
    sqr2Color: '#5e35b1',
    sqr3Color: '#ff9800',
    sqr4Color: '#03a9f4',
  },
});

export default theme;
