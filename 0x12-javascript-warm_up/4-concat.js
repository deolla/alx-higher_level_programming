#!/usr/bin/node
// A script that prints two arguments passed to it, in the following format: “ is ”

const process = require('process');
const args = process.argv.slice(2);

console.log(args[0] + ' ' + 'is' + ' ' + args[1]);
