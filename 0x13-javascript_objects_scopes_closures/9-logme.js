#!/usr/bin/node
let argcnt = 0;
exports.logMe = function (item) { console.log(`${argcnt++}: ${item}`); };
