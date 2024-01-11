#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 100-starwars_characters.js <movie-id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);

      // Check if movie data includes characters
      if (movieData.characters && movieData.characters.length > 0) {
        // Fetch and display character names in the order of the list "characters"
        const charactersUrls = movieData.characters;
        charactersUrls.forEach((characterUrl) => {
          request.get(characterUrl, (characterError, characterResponse, characterBody) => {
            if (!characterError) {
              const characterData = JSON.parse(characterBody);
              console.log(characterData.name);
            } else {
              console.error(characterError);
            }
          });
        });
      } else {
        console.log('No characters found for this movie.');
      }
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
