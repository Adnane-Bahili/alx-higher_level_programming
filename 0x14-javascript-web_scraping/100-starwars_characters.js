#!/usr/bin/node
require('request')('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (errors, response, body) {
  if (!errors) {
    JSON.parse(body).characters.forEach(function (char) {
      require('request')(char, function (errors, response, body) {
        if (!errors) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
