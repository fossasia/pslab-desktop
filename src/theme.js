import { createMuiTheme } from '@material-ui/core/styles';

const theme = createMuiTheme({
  palette: {
    common: {
      black: '#000',
      white: '#fff',
    },
    background: {
      paper: 'rgba(255, 255, 255, 1)',
      default: 'rgba(181, 181, 181, 0.2)',
    },
    primary: {
      light: '#ff6659',
      main: '#d32f2f',
      dark: '#9a0007',
      contrastText: '#fff',
    },
    secondary: {
      light: '#757de8',
      main: '#3f51b5',
      dark: '#002984',
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
    gradient1:
      'linear-gradient(90deg, rgba(207,72,139,1) 5%, rgba(101,101,163,1) 48%, rgba(79,77,175,1) 100%)',
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
