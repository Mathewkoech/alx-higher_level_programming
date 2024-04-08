#!/usr/bin/node
const x = process.argv[2];
const y = process.argv[3];
function add (x, y) {
  return (x + y);
}
console.log(add(parseInt(x), parseInt(y)));
