#!/usr/bin/node

exports.converter = function (base) {
  function convert (i) {
    return i.toString(base);
  }
  return convert;
};
