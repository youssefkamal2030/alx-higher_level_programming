#!/usr/bin/node
exports.esrever = function (list) {
  const ans = [];
  for (let i = list.length - 1; i >= 0; i--) {
    ans.push(list[i]);
  }
  return ans;
};
