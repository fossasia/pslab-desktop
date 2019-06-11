exports.oscilloscopeVoltageProcessor = parsedJSON => {
  const { data } = parsedJSON;
  const { keys } = parsedJSON;
  const { numberOfChannels } = parsedJSON;
  const numberOfDataPoints = data.length;

  let parsedOutput = [];

  switch (numberOfChannels) {
    case 1:
      try {
        for (let index = 0; index < numberOfDataPoints; index += 1) {
          parsedOutput = [
            ...parsedOutput,
            {
              [keys[0]]: data[index][0],
              [keys[1]]: data[index][1],
            },
          ];
        }
      } catch (error) {
        return false;
      }
      break;
    case 2:
      try {
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
      } catch (error) {
        return false;
      }

      break;
    case 3:
      try {
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
      } catch (error) {
        return false;
      }

      break;
    case 4:
      try {
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
      } catch (error) {
        return false;
      }

      break;
    default:
      break;
  }

  return parsedOutput;
};

exports.oscilloscopeXYProcessor = parsedJSON => {
  const { data } = parsedJSON;
  const { keys } = parsedJSON;
  const numberOfDataPoints = data.length;

  let parsedOutput = [];
  if (data[0][0] === undefined || data[0][1] === undefined) {
    return false;
  }
  for (let index = 0; index < numberOfDataPoints; index += 1) {
    parsedOutput = [
      ...parsedOutput,
      {
        [keys[0]]: data[index][0],
        [keys[1]]: data[index][1],
      },
    ];
  }

  return parsedOutput;
};
