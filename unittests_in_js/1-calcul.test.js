// 1-calcul.test.js
const assert = require("assert");
const calculateNumber = require("./1-calcul");
describe("calculateNumber", function () {
  describe("SUM", function () {
    it("should return 6 when given 1.4 and 4.5", function () {
      assert.strictEqual(calculateNumber(1.4, 4.5, "SUM"), 6);
    });
    it("should return 5 when given 1.5 and 3.7", function () {
      assert.strictEqual(calculateNumber(1.5, 3.7, "SUM"), 6);
    });
  });
  describe("SUBTRACT", function () {
    it("should return -5 when given 1.4 and 5.5", function () {
      assert.strictEqual(calculateNumber(1.4, 5.5, "SUBTRACT"), -5);
    });
    it("should return -2 when given 1.5 and 3.7", function () {
      assert.strictEqual(calculateNumber(1.5, 3.7, "SUBTRACT"), -2);
    });
  });
  describe("DIVIDE", function () {
    it("should return 0.2 when given 1.4 and 5.4", function () {
      assert.strictEqual(calculateNumber(1.4, 5.4, "DIVIDE"), 0.2);
    });
    it("should return 'Error' when dividing by 0", function () {
      assert.strictEqual(calculateNumber(1.5, 0.4, "DIVIDE"), "Error");
    });
  });
});
