#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const movies = JSON.parse(data).results;
      const numMovies = movies.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count;
      }, 0);
      console.log(numMovies);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
