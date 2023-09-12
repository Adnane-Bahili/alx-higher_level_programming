#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let Row = '';
    for (let count = 0; count < size; count++) Row += 'X';
    console.log(Row);
  }
}
