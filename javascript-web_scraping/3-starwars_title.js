#!/usr/bin/node

const request = require('request');
url_sw = 'https://swapi-api.hbtn.io/api/films/:id';

request.get(url_sw, process.argv[2], 
  function (err, response, body) {
    if (err) {
      console.log(err)
    }
    console.log(JSON.parse(body).title);
});
