#!/usr/bin/node
function add (i, j) {
  return i + j;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
