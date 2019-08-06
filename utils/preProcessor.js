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

exports.LAProcessor = parsedJSON => {
  const {
    time1,
    voltage1,
    time2,
    voltage2,
    time3,
    voltage3,
    time4,
    voltage4,
  } = parsedJSON;
  const { numberOfChannels } = parsedJSON;

  let parsedOutput = {
    LA1Data: null,
    LA2Data: null,
    LA3Data: null,
    LA4Data: null,
  };
  if (numberOfChannels >= 1) {
    parsedOutput.LA1Data = [];
    time1.map((time, index) => {
      parsedOutput.LA1Data = [
        ...parsedOutput.LA1Data,
        {
          voltage: voltage1[index],
          time,
        },
      ];
    });
  }
  if (numberOfChannels >= 2) {
    parsedOutput.LA2Data = [];
    time2.map((time, index) => {
      parsedOutput.LA2Data = [
        ...parsedOutput.LA2Data,
        {
          voltage: voltage2[index],
          time,
        },
      ];
    });
  }
  if (numberOfChannels >= 3) {
    parsedOutput.LA3Data = [];
    time3.map((time, index) => {
      parsedOutput.LA3Data = [
        ...parsedOutput.LA3Data,
        {
          voltage: voltage3[index],
          time,
        },
      ];
    });
  }
  if (numberOfChannels >= 4) {
    parsedOutput.LA4Data = [];
    time4.map((time, index) => {
      parsedOutput.LA4Data = [
        ...parsedOutput.LA4Data,
        {
          voltage: voltage4[index],
          time,
        },
      ];
    });
  }

  return parsedOutput;
};
