#!/usr/bin/node
exports.esrever = function (list) {
  const rever = [];
  for (let r = list.length - 1; r >= 0; --r) {
    rever.push(list[r]);
  }
  return rever;
};
