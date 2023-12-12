#!/usr/bin/node

const fs = require('fs');

const fileAPath = fs.readFileSync(process.argv[2]).toString();
const fileBPath = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fileAPath + fileBPath);
