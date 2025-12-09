// 0-calcul.test.js
const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("should return 5 when given 1.4 and 3.6", function () {
    assert.strictEqual(calculateNumber(1.4, 3.6), 5);
  });
  it("should return 6 when given 1.5 and 3.5", function () {
    assert.strictEqual(calculateNumber(1.5, 3.5), 6);
  });
  it("should return 0 when given 0 and 0", function () {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
  it("should return -4 when given -1.4 and -2.6", function () {
    assert.strictEqual(calculateNumber(-1.4, -2.6), -4);
  });
  it("should return 0 when given -1.5 and 1.5", function () {
    assert.strictEqual(calculateNumber(-1.5, 1.5), 0);
  });
});
