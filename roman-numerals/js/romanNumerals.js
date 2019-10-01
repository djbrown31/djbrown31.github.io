exports.toRoman = {
  const toRoman = function (num, output) {
    const numerals = {
      'M': 1000,
      'CM': 900,
      'D': 500,
      'CD': 400,
      'C': 100,
      'XC': 90,
      'L': 50,
      'XL': 40,
      'X': 10,
      'IX': 9,
      "V": 5,
      'IV': 4,
      'I': 1
    };
    let str = output;
    if (num == 0) {
      return str;
    }
    for (let key in numerals) {
      if (num - numerals[key] >= 0) {
        str += key;
        return toRoman(num - numerals[key], str);
      }
    }
  };
  
  module.exports = toRoman
};
var toRoman = require("./romanNumerals");

