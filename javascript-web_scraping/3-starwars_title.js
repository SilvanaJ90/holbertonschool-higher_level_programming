#!/usr/bin/node

const request = require('request');
url_sw = 'https://swapi-api.hbtn.io/api/films/:id';
first_argv = process.argv[2];

request.get(url_sw, function (err, response) {
  if (err) {
    return;
  }
  console.log(first_argv);
});
