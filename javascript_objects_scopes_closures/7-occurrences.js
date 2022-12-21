#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let acc = 0;
  for (let elem = 0; elem < list.length; elem++) {
    if (list[elem] === searchElement) {
      acc++
    }
  }
  return acc;
}
