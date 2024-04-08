#!/usr/bin/node
const [,, arg] = process.argv;
const number = parseInt(arg);
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
