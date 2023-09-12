#!/usr/bin/node
// Write a function that prints the number of arguments already printed and the new argument value. (see example below).

let m = 0;
exports.logMe = function (item) {
  m++;
  console.log(`${m}: ${item}`);
};
