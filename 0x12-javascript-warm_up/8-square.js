#!/usr/bin/node
const count = process.argv;
const x = parseInt(count[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let print = '';
    for (let j = 0; j < x; j++) print += 'X';
    console.log(print);
  }
}
