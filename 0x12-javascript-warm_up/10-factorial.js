#!/usr/bin/node
// A script that computes and prints a factorial.
// The first argument is integer (argument can be cast as integer) used for computing the factorial.
// Factorial of NaN is 1
// You must do it recursively.
// You must use a function.

const process = require('process');
const args = process.argv.slice(2);

const arg = parseInt(args[0]);

function factorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  }
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const fact = factorial(arg);
console.log(fact);
