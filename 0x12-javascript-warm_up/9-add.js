#!/usr/bin/node
// A script that prints the addition of 2 integers.
// The first argument is the first integer.
// The second argument is the second integer.
// You have to define a function with this prototype: function add(a, b).

const process = require('process');
const args = process.argv.slice(2);

const firstArg = parseInt(args[0]);
const secondArg = parseInt(args[1]);

function add (a, b) {
  return a + b;
}

if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  const sum = add(firstArg, secondArg);
  console.log(sum);
}
