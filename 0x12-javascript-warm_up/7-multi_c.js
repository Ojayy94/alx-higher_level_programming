#!/usr/bin/node
const count = process.argv;
const x = parseInt(count[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');}
}
