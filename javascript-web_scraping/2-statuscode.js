#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response) {
  if (err) {
    return;
  }
  console.log('code: ' +  response.statusCode);
});