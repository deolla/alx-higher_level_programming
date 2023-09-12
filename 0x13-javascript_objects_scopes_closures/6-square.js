#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square of 5-square.js:
// You must use the class notation for defining your class and extends.
// reate an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X.

const Rectangle = require('./4-Rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str = '';
    if (c === undefined) {
      for (let x = 0; x < this.width; x++) {
        str = '';
        for (let m = 0; m < this.height; m++) {
          str += 'X';
        }
        console.log(str);
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        str = '';
        for (let j = 0; j < this.height; j++) {
          str += 'C';
        }
        console.log(str);
      }
    }
  }
}
module.exports = Square;
