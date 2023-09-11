#!/usr/bin/node
// Write a function that increments and calls a function.
// The function must be visible from outside.

function addMeMaybe (number, theFunction) {
  const increment = number + 1;
  theFunction(increment);
}

module.exports.addMeMaybe = addMeMaybe;
