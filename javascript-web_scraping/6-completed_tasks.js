#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const task = {};
    for (const i of todos) {
      if (i.completed === true) {
        if (i.userId in task) {
          task[i.userId]++;
        } else {
          task[i.userId] = 1;
        }
      }
    }
    console.log(task);
  }
});
