#!/usr/bin/node
count = process.argv;
const myNum = parseInt(count[2]);

if (myNum) {
  console.log('My number: ' + myNum);
} else if (myNum === NaN) {
  console.log('Not a number');
} else {
  console.log('Not a number');
}
