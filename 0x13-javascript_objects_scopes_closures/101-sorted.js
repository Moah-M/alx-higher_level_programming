#!/usr/bin/node

const { dict } = require('./101-data.js');
const newD = {};
for (const N in dict) {
  if (newD[dict[N]] === undefined) {
    newD[dict[N]] = [];
  }
  newD[dict[N]].push(N);
}
console.log(newD);
