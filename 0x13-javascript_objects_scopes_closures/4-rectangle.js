#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// Create an instance method called rotate() that exchanges the width and the height of the rectangle.
// Create an instance method called double() that multiples the width and the height of the rectangle by 2

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
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

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
