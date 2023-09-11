#!/usr/bin/node
// Write a function that executes x times a function.
// The function must be visible from outside.

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;
