#!/usr/bin/node
const fs = require('fs');
const request = require('request');
// Make an HTTP GET request using the 'request' module to the URL provided as the third command-line argument (process.argv[2]).
// The response from the request is piped (transferred) to a writable stream created by 'fs.createWriteStream',
// which writes the content to a file specified as the fourth command-line argument (process.argv[3]).
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
