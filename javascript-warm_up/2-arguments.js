#!/usr/bin/node
let Args = process.argv.length - 2;

if (Args == 0) {
  console.log(ii'No argument');
} else if (Args == 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found')
}
