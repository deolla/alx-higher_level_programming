#!/usr/bin/node
// A script that prints a square.
// The first argument is the size of the square.

const process = require('process');
const args = process.argv.slice(2);

const sizeSquare = parseInt(args[0]);

if (isNaN(sizeSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeSquare; i++) {
    let str = '';
    for (let m = 0; m < sizeSquare; m++) {
      str += 'X';
    }
    console.log(str);
  }
}
