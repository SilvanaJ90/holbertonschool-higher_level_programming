#!/usr/bin/node

const request = require('request');
url_sw = 'https://swapi-api.hbtn.io/api/films/:id';

request.get(url_sw, process.argv[2], 
  function (err, response) {
  if (err) {
    return;
  }
  console.log(JSON.parse(response).title);
});
