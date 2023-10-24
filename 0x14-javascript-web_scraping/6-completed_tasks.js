#!/usr/bin/node
const done = {};
require('request').get(process.argv.slice(2)[0], function (errors, response, body) {
  if (errors) throw errors;
  for (let l = 0; l < JSON.parse(body).length; l++) {
    const key = JSON.parse(body)[l].userId;
    if (JSON.parse(body)[l].completed) {
      if (!(key in done)) {
        done[key] = 1;
      } else {
        done[key] += 1;
      }
    }
  }
  console.log(done);
});
