#!/usr/bin/node

const dict = require('./101-data').dict;

const valuesArray = Object.values(dict).sort((a, b) => a - b);

const keysByValue = {};

for (const key in dict) {
    const value = dict[key];

    if (!keysByValue[value]) {
        keysByValue[value] = [];
    }

    keysByValue[value].push(key);
}

console.log('Sorted Values:', valuesArray);
console.log('Keys by Value:', keysByValue);
