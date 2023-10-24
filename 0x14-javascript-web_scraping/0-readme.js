#!/usr/bin/node
require('fs').readFile(process.argv[2], 'utf8', function (errors, filecont) {
  console.log(errors || filecont);
});
