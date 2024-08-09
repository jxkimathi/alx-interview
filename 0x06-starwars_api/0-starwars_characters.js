#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/'

if (process.argv.length > 2) {
  const movieId = process.argv[2];

    // Request the film data from the API
    request(`${url}/films/${movieId}/`, (err, response, body) => {
      if (err) {
        return console.error(err);
      }
      if (response.statusCode === 200) {
        // Parse the response body to get character URLs
        const charactersURLs = JSON.parse(body).characters;
  
        // Create an array of promises to fetch character names
        const characterPromises = charactersURLs.map(url => {
          return new Promise((resolve, reject) => {
            request(url, (error, res, charBody) => {
              if (error) {
                reject(error);
              } else {
                // Resolve the promise with the character's name
                resolve(JSON.parse(charBody).name);
              }
            });
          });
        });

        // Wait for all promises to resolve
        Promise.all(characterPromises)
        .then(names => {
          names.forEach(name => console.log(name));
        })
        .catch(error => console.error(error));
      } else {
        console.error(`Failed to get film data: Status Code, ${response.statusCode}`);
      }
    });
  } else {
    console.log('Usage: ./0-starwars_characters.js <movie_id>');  
}
