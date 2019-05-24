exports.oscilloscopeDataProcessor = parsedJSON => {
  const { data } = parsedJSON;
  const { keys } = parsedJSON;
  const { numberOfChannels } = parsedJSON;
  const numberOfDataPoints = data.length;

  let parsedOutput = [];

  switch (numberOfChannels) {
    case 1:
      for (let index = 0; index < numberOfDataPoints; index += 1) {
        parsedOutput = [
          ...parsedOutput,
          {
            [keys[0]]: data[index][0],
            [keys[1]]: data[index][1],
          },
        ];
      }
      break;
    case 2:
      for (let index = 0; index < numberOfDataPoints; index += 1) {
        parsedOutput = [
          ...parsedOutput,
          {
            [keys[0]]: data[index][0],
            [keys[1]]: data[index][1],
            [keys[2]]: data[index][2],
          },
        ];
      }
      break;
    case 3:
      for (let index = 0; index < numberOfDataPoints; index += 1) {
        parsedOutput = [
          ...parsedOutput,
          {
            [keys[0]]: data[index][0],
            [keys[1]]: data[index][1],
            [keys[2]]: data[index][2],
            [keys[3]]: data[index][3],
          },
        ];
      }
      break;
    case 4:
      for (let index = 0; index < numberOfDataPoints; index += 1) {
        parsedOutput = [
          ...parsedOutput,
          {
            [keys[0]]: data[index][0],
            [keys[1]]: data[index][1],
            [keys[2]]: data[index][2],
            [keys[3]]: data[index][3],
            [keys[4]]: data[index][4],
          },
        ];
      }
      break;
    default:
      break;
  }

  return parsedOutput;
};
