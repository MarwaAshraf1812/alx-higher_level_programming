#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.alx.tools/api/films/' + process.argv[2];

request.get(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const content = JSON.parse(data);
    console.log(content.title);
  } else {
    console.error('Error code: ' + res.statusCode);
  }
});
