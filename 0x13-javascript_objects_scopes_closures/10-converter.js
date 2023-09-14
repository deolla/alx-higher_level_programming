#!/usr/bin/node
// Write a function that converts a number from base 10 to another base passed as argument:
// You are not allowed to import any file
// You are not allowed to declare any new variable (var, let, etc..)

exports.converter = function (base) {
  if (base < 2 || base > 36) {
    return;
  }
  return function convertToBase (num) {
    if (num < base) {
      return num.toString(base);
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base).toString(base);
    }
  };
};
