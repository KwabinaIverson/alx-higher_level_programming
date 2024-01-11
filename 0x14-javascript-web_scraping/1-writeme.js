#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const writeString = process.argv[3];

if (!filePath || !writeString) {
  console.error('Usage: node 1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

fs.writeFile(filePath, writeString, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
