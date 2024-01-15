#!/usr/bin/node

const request = require('request');

/**
 * Function to fetch and print characters of a Star Wars movie.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function getStarWarsCharacters (movieId) {
  // API endpoint URL
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // Making a request to the Star Wars API to get movie data
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Parsing the response body as JSON
    const filmData = JSON.parse(body);

    // Extracting the characters list from the film data
    const characters = filmData.characters;

    // Array to store promises for individual character requests
    const characterPromises = characters.map(characterUrl => new Promise((resolve, reject) => {
      // Making a request to the Star Wars API to get individual character data
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        }

        // Parsing character data as JSON
        const characterData = JSON.parse(charBody);

        // Resolving the promise with the character name
        resolve(characterData.name);
      });
    }));

    // Wait for all character promises to resolve
    Promise.all(characterPromises)
      .then(names => {
        // Displaying characters one per line
        console.log(names.join('\n'));
      })
      .catch(allErr => console.log(allErr));
  });
}

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Call the function with the provided movie ID
getStarWarsCharacters(movieId);
