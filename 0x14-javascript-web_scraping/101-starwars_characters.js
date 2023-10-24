#!/usr/bin/node
require('request')('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (errors, response, body) {
  if (!errors) {
    printCharacters(JSON.parse(body).characters, 0);
  }
});
function printCharacters (char, idx) {
  require('request')(char[idx], function (errors, response, body) {
    if (!errors) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < char.length) {
        printCharacters(char, idx + 1);
      }
    }
  });
}
