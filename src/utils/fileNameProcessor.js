export const fileNameTrimmer = (n, len) => {
  const ext = n.substring(n.lastIndexOf('.') + 1, n.length).toLowerCase();
  let filename = n.replace('.' + ext, '');
  if (filename.length <= len) {
    return n;
  }
  filename = filename.substr(0, len) + (n.length > len ? '...' : '');
  return filename + '.' + ext;
};

export const extractFileName = filePath => {
  const fileArray = filePath.split('/');
  return fileArray[fileArray.length - 1];
};
