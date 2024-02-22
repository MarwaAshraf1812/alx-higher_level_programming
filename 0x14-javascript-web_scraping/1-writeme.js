#!/usr/bin/node

// Reading a file using the fs module.
const fs = require('fs');
const args = process.argv;
fs.writeFile(args[2], args[3], 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
