#!/usr/bin/node

const dict = require('./101-data').dict;

const valuesArray = Object.values(dict);
valuesArray.sort((a, b) => a - b);
keysByValue = {};
for (const key in dict) {
  const value = dict[key];
  if (!keysByValue[value]) {
    keysByValue[value] = [];
  }
  keysByValue[value].push(key);
}

