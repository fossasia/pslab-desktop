// The label background color is a workaround for issues with line through text
// see https://github.com/mui-org/material-ui/issues/14530#issuecomment-463576879
// The padding and negative margin allow for a little spacing whilst retaining
// the alignment.
export default theme => ({
  formControl: {
    margin: '0px 0px 0px 16px',
  },
  label: {
    margin: '0 -4px',
    padding: '0 4px',
    backgroundColor: 'white',
  },
});
