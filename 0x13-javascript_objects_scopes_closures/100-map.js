#!/usr/bin/node

const myList = require('./100-data');

function mapIndex (myList) {
  return myList.map((x, index) => x * index);
}
console.log(myList);
console.log(mapIndex(myList));
