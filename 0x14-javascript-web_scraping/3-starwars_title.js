#!/usr/bin/node
require('request')('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (errors, response, body) {
  console.log(errors || JSON.parse(body).title);
});
