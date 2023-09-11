#!/usr/bin/node
// A script that prints the first argument passed to it:
// If no arguments are passed to the script, print “No argument”
// You must use console.log(...) to print all output.

const process = require('process');
const args = process.argv.slice(2);

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No arguments');
}
