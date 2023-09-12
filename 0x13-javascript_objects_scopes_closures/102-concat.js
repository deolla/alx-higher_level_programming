#!/usr/bin/node
// Write a script that concats 2 files
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination.

const fs = require('fs');

const process = require('process');
const argv = process.argv;

const firstArg = fs.readFileSync(argv[2]).toString();
const secondArg = fs.readFileSync(argv[3]).toString();
fs.writeFileSync(argv[4], firstArg + secondArg);
