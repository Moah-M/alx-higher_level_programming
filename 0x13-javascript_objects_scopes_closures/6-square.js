#!/usr/bin/node

const Square2 = require('./5-square');

module.exports = class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
};
