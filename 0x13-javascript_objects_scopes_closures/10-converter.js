#!/usr/bin/node

exports.converter = function (base) {
  return function (numberToConvert) {
    return numberToConvert.toString(base);
  };
};
