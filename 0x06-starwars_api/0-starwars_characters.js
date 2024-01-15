#!/usr/bin/node

const request = require('request');

/**
 * Function to fetch and print characters of a Star Wars movie.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function getStarWarsCharacters (movieId) {
  // API endpoint URL
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  // Making a request to the Star Wars API
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Parsing the response body as JSON
    const filmData = JSON.parse(body);

    // Extracting the characters list from the film data
    const characters = filmData.characters;

    // Displaying characters one per line
    characters.forEach((characterUrl) => {
      // Extracting character ID from the character URL
      const characterId = characterUrl.split('/').filter(Boolean).pop();

      // Fetching individual character data
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character:', charError);
          return;
        }

        // Parsing character data as JSON
        const characterData = JSON.parse(charBody);

        // Displaying the character name
        console.log(characterData.name);

        // Check if it's the last character, then print a newline
        if (characterId === characters[characters.length - 1].split('/').filter(Boolean).pop()) {
          console.log();
        }
      });
    });
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
