#!/usr/bin/node
const [,, args] = process.argv;
if (!args) {
  console.log('No argument');
} else {
  console.log(args);
}
