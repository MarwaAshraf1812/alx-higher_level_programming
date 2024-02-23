#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const content = JSON.parse(data);
    console.log(content.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
