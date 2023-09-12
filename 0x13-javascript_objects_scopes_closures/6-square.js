#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square of 5-square.js:
// You must use the class notation for defining your class and extends.
// reate an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X.

const SquareU = require('./5-square');

class Square extends SquareU {
  charPrint (c) {
    let str = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.width; x++) {
      str = '';
      for (let m = 0; m < this.height; m++) {
        str += c;
      }
      console.log(str);
    }
  }
}
module.exports = Square;
