#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 6-completed_tasks.js <api-url>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const todos = JSON.parse(body);

      // Filter completed tasks and count by user ID
      const completedTasksByUser = todos.reduce((result, todo) => {
        if (todo.completed) {
          result[todo.userId] = (result[todo.userId] || 0) + 1;
        }
        return result;
      }, {});

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
