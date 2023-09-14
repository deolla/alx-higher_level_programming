#!/usr/bin/node
// A script that prints My number: <first argument converted in integer>.

const process = require('process');
const args = process.argv.slice(2);
const numArg = parseInt(args[0]);

if (isNaN(numArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numArg}`);
}
