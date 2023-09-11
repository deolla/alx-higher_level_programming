#!/usr/bin/node
// A script that prints a message depending of the number of arguments passed:
// If no arguments are passed to the script, print “No argument”
// If only one argument is passed to the script, print “Argument found”
// Otherwise, print “Arguments found”.

const process = require('process');
const args = process.argv.slice(2);

let output;

if (args.length === 0) {
  output = 'No argument';
} else if (args.length === 1) {
  output = 'Argument found';
} else {
  output = 'Arguments found';
}
console.log(output);
