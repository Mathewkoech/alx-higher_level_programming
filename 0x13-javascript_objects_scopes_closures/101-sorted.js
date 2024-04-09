#!/usr/bin/node
const dict = require('./101-data.js').dict;

const dictt = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (dictt[dict[occurences]] === undefined) {
    dictt[dict[occurences]] = [occurences];
  } else {
    dictt[dict[occurences]].push(occurences);
  }
});
console.log(dictt);
