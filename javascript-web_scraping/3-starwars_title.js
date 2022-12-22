#!/usr/bin/node

const request = require('request');
url_s = 'https://swapi-api.hbtn.io/api/films/';
args = process.argv[2]

request.get(url_s + args, function (err, request, body) {
  if (err) {
    console.log(err)
  } else {
    console.log(JSON.parse(body).title);
  }
});
