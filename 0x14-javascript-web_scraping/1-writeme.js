#!/usr/bin/node
require('fs').writeFile(process.argv[2], process.argv[3], function (errors) {
  if (errors) console.log(errors);
});
