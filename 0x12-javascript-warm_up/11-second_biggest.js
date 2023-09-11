#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments..
// You can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0
const process = require('process');
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  let maxNum = parseInt(args[0]);
  let secMax = parseInt(args[1]);

  if (secMax > maxNum) {
    [maxNum, secMax] = [secMax, maxNum];
  }

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > maxNum) {
      secMax = maxNum;
      maxNum = num;
    } else if (num > secMax && num !== maxNum) {
      secMax = num;
    }
  }
  console.log(secMax);
}
