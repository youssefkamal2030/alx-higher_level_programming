#!/usr/bin/node
const x = parseInt(process.argv[2]);
const ans = (a) => {
  if (isNaN(a) || a === 0) { return 1; }
  return a * ans(a - 1);
};
console.log(ans(x));
