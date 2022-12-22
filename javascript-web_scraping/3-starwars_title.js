#!/usr/bin/node

const request = require('request');
url_sw = 'https://swapi-api.hbtn.io/api/films/';

request.get(url_sw + process.argv[2], function (err, request, body) { 
  if (err) {
   console.log(err)
  } else {
   console.log(JSON.parse(body).title);
  }
});
