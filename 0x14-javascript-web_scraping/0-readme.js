#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
