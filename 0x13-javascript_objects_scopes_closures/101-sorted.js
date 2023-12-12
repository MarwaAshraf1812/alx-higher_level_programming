#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = {};
for (const key in dict) {
  const value = dict[key];
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}

console.log(newDict);