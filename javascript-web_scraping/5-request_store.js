#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, function (error, res, body) {
  if (error) {
    console.log(err);
  }
  fs.writeFile(filename, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
