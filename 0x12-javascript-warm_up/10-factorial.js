#!/usr/bin/node

const args = process.argv;
const numb = parseInt(args[2]);

function fact (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}
console.log(fact(numb));
