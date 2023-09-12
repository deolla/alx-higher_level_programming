#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
// Your script must import dict from the file 101-data.js.

const importedDict = require('./101-data').dict;

const entries = Object.entries(importedDict);
const data = Object.values(importedDict);
const uniqueValues = [...new Set(data)];
const newDictionary = {};

for (const p in uniqueValues) {
  const userList = [];
  for (const y in entries) {
    if (entries[y][1] === uniqueValues[p]) {
      userList.unshift(entries[y][0]);
    }
  }
  newDictionary[uniqueValues[p]] = userList;
}
console.log(newDictionary);
