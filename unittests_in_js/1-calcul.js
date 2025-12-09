// 1-calcul.js
"use strict";

function calculateNumber(a, b, type) {
  if (type === "SUM") {
    return Math.round(a) + Math.round(b);
  } else if (type === "SUBTRACT") {
    return Math.round(a) - Math.round(b);
  } else if (type === "DIVIDE") {
    if (Math.round(b) === 0) {
      return "Error";
    }
    return Math.round(a) / Math.round(b);
  }
}
module.exports = calculateNumber;
