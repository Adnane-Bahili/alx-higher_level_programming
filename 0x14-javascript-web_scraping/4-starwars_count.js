#!/usr/bin/node
require('request')(process.argv[2], function (errors, response, body) {
  if (!errors) {
    console.log(JSON.parse(body).results.reduce(function (count, mv) {
      return mv.characters.find((char) => char.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
