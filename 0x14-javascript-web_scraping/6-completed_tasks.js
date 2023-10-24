#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    try {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      for (const todo of todos) {
        if (todo.completed) {
          const userId = todo.userId;
          if (completedTasksByUser[userId]) {
            completedTasksByUser[userId]++;
          } else {
            completedTasksByUser[userId] = 1;
          }
        }
      }

      console.log(completedTasksByUser);
    } catch (error) {
      console.log(error);
    }
  }
});
