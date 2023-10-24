#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    try {
      const films = JSON.parse(body).results;
      let movieCount = 0;

      const fetchCharacter = (url) => {
        return new Promise((resolve, reject) => {
          request.get(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else if (response.statusCode !== 200) {
              reject(new Error(response.statusCode));
            } else {
              const character = JSON.parse(body);
              resolve(character);
            }
          });
        });
      };

      const checkMovies = async () => {
        for (const film of films) {
          const characters = film.characters;
          for (const characterUrl of characters) {
            const character = await fetchCharacter(characterUrl);
            if (character.url === `https://swapi-api.alx-tools.com/api/people/${characterId}/`) {
              movieCount++;
              break;
            }
          }
        }
        console.log(movieCount);
      };

      checkMovies();
    } catch (error) {
      console.log(error);
    }
  }
});
