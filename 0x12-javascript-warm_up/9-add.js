#!/usr/bin/node

const x = (a, b) => {
  return a + b;
};
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
if (!isNaN(a) && !isNaN(b)) {
  console.log(x(a, b));
} else {
  console.log('NaN');
}
