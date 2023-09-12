#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let m = 0; m < this.width; m++) {
          str += 'X';
	}
        console.log(str);
      }
    }
  }
}
module.exports = Rectangle;
