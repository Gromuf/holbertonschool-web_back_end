// 2-calcul_chai.test.js
const expect = require("chai").expect;
const calculateNumber = require("./2-calcul_chai");
describe("calculateNumber", function () {
  describe("SUM", function () {
    it("should return 6 when given 1.4 and 4.5", function () {
      expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });
    it("should return 5 when given 1.5 and 3.7", function () {
      expect(calculateNumber("SUM", 1.5, 3.7)).to.equal(6);
    });
  });
  describe("SUBTRACT", function () {
    it("should return -5 when given 1.4 and 5.5", function () {
      expect(calculateNumber("SUBTRACT", 1.4, 5.5)).to.equal(-5);
    });
    it("should return -2 when given 1.5 and 3.7", function () {
      expect(calculateNumber("SUBTRACT", 1.5, 3.7)).to.equal(-2);
    });
  });
  describe("DIVIDE", function () {
    it("should return 0.2 when given 1.4 and 5.4", function () {
      expect(calculateNumber("DIVIDE", 1.4, 5.4)).to.equal(0.2);
    });
    it("should return 'Error' when dividing by 0", function () {
      expect(calculateNumber("DIVIDE", 1.5, 0.4)).to.equal("Error");
    });
  });
});
