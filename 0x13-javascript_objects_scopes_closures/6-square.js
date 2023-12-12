#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    const charPrint = c || 'X';
    while (i < this.height) {
      console.log(charPrint.repeat(this.width));
      i++;
    }
  }
}
module.exports = Square;
