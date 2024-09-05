#!/usr/bin/node
const request = require("request");
const id = process.argv[2];

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

request(
  `https://swapi-api.alx-tools.com/api/films/${id}`,
  (error, response, body) => {
    if (error) {
      console.error("Error:", error);
    }
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(async function (character, index) {
      const person = await makeRequest(character);
      console.log(`${index}-${person.name}`);
    });
  }
);
