export default function roundOff(num, roundTo = 2) {
  num = parseFloat(num);
  return +num.toFixed(roundTo);
}
