#!/usr/bin/node

const request = require('request');

const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  fc.writeFile(process.argv[3], body, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
});
});
