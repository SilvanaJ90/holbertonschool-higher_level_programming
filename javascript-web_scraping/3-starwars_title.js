#!/usr/bin/node

const request = require('request');
url_sw = 'https://swapi-api.hbtn.io/api/films/:id';

request.get(url + process.argv[2], (err, res, body) => { 
  if (err) {
   console.log(err)
  } else {
   console.log(JSON.parse(body).title);
  }
});
