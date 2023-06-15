#!/usr/bin/node
let Args = process.argv.length - 2;

if (Args == 0) {
  console.log('0 arguments');
} else if (Args == 1) {
  console.log('1 Argument found');
} else {
  console.log('Arguments found')
}
