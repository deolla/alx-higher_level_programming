#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
