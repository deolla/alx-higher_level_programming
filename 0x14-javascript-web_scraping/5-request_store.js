#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.errror(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
      if (error) {
        console.error(error);
      } else {
        console.log('Successfully saved the webpage content to the file.');
      }
    });
  }
});
