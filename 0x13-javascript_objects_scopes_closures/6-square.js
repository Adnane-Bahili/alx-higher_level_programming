#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    if (c === undefined) {
      this.print(c);
    } else {
      for (let n = 0; n < this.height; n++) console.log(c.repeat(this.width));
    }
  }
};
