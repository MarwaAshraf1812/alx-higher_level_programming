#!/usr/bin/node

exports.esrever = function (list) {
  const listF = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listF.push(list[i]);
  }
  return listF;
};
