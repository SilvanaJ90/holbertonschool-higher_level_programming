#!/usr/bin/node

const request = require('request');
url_sw = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], (err, body) => { 
  if (err) {
   console.log(err)
  } else {
   console.log(JSON.parse(body).title);
  }
});
