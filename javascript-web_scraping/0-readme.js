#!/usr/bin/node

var fs = require("fs");
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function(err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
