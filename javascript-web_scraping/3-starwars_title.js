#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:18';
const moveId = process.argv[2];

request.get(url + moveId, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).person=18);
  }
});
