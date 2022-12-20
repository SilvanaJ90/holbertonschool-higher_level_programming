#!/usr/bin/node

function factorialize (num) {
  if (num === 0 || num === 1 || isNaN(num))
    return 1;
  for (let i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
console.log(factorialize(parseInt(process.argv[2])));
