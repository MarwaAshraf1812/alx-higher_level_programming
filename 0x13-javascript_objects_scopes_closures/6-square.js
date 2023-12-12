#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
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
