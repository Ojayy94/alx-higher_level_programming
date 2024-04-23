#!/usr/bin/node

const request = require('request');

request.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write(data);
  }
});
