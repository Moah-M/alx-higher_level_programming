#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  while (list.length > 0) {
    revlist.push(list.pop());
  }
  return revlist;
};
