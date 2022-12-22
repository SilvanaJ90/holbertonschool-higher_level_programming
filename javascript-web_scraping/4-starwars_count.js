#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const moveId = 'https://swapi-api.hbtn.io/api/people/18';

request.get(url, function (err, res, body) {
  if (moveId) {
    count++
  return count
  }
});
console.log(count);
