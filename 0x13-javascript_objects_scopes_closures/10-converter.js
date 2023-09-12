#!/usr/bin/node
exports.converter = function (base) {
  return numBase => numBase.toString(base);
};
