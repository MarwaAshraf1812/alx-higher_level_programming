#!/usr/bin/node

const args = process.argv;

if (!args[3]) {
  console.log(NaN);
} else {
  add(parseInt(args[2]), parseInt(args[3]));
}
function add (arg2, arg3) {
  console.log(arg2 + arg3);
}
