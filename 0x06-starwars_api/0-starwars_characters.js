#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, idx) {
  const charUrl = characters[idx];
  request(charUrl, function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      body = JSON.parse(body).name;
      console.log(body);
      if (idx + 1 < characters.length) {
        printChars(characters, idx + 1);
      }
    }
  });
}
