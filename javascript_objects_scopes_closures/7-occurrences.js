#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {

  list.reduce((acc, elem) => {
    return (searchElement === elem ? acc + 1 : acc)
  });
};