#!/usr/bin/node
require('request').get(process.argv[2]).on('response', function (restacode) {
  console.log(`code: ${restacode.statusCode}`);
});
