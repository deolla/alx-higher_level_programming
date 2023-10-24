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

      const fetchCharacter = (url) => {
        return new Promise((resolve, reject) => {
          request.get(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else if (response.statusCode !== 200) {
              reject(new Error(`Request failed with status code ${response.statusCode}`));
            } else {
              const character = JSON.parse(body);
              resolve(character.name);
            }
          });
        });
      };

      const printCharacters = async () => {
        for (const characterUrl of characters) {
          try {
            const characterName = await fetchCharacter(characterUrl);
            console.log(characterName);
          } catch (error) {
            console.log(error);
          }
        }
      };

      printCharacters();
    } catch (error) {
      console.log(error);
    }
  }
});
