#!/usr/bin/node
const request = require('request')
request({
  // will be ignored
  method: 'GET',
  uri: 'http://www.google.com',

  // HTTP Archive Request Object
  har: {
    url: 'http://www.mockbin.com/har',
    method: 'POST',
    headers: [
      {
        name: 'content-type',
        value: 'application/x-www-form-urlencoded'
      }
    ],
    postData: {
      mimeType: 'application/x-www-form-urlencoded',
      params: [
        {
          name: 'foo',
          value: 'bar'
        },
        {
          name: 'hello',
          value: 'world'
        }
      ]
    }
  }
})