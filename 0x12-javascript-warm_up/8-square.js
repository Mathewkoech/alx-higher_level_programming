#!/usr/bin/node
const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let myVar = '';
    let y = 0;

    while (y < x) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
