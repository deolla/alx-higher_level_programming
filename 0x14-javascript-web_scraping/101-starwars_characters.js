#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request.get(apiUrl + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    try {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      const printCharacters = (index) => {
        if (index >= characters.length) {
          return;
        }

        const characterUrl = characters[index];
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.log(error);
          } else if (response.statusCode !== 200) {
            console.log(response.statusCode);
          } else {
            try {
              const character = JSON.parse(body);
              console.log(character.name);
            } catch (error) {
              console.log(error);
            }
          }

          printCharacters(index + 1);
        });
      };

      printCharacters(0);
    } catch (error) {
      console.log(error);
    }
  }
});
