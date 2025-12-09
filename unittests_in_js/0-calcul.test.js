// 0-calcul.test.js
const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("1 + 3", () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it("1 + 3.7 = 5", () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it("1.2 + 3.7 = 5", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it("1.5 + 3.7 = 6", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  const values = [
    -5.9, -5.5, -5.4, -5.1, -5.0, -4.9, -4.5, -4.4, -4.1, -4.0, -3.9, -3.5,
    -3.4, -3.1, -3.0, -2.9, -2.5, -2.4, -2.1, -2.0, -1.9, -1.5, -1.4, -1.1,
    -1.0, -0.9, -0.5, -0.4, -0.1, -0.0, 0.0, 0.1, 0.4, 0.5, 0.9, 1.0, 1.1, 1.4,
    1.5, 1.9, 2.0, 2.1, 2.4, 2.5, 2.9, 3.0, 3.1, 3.4, 3.5, 3.9, 4.0, 4.1, 4.4,
    4.5, 4.9, 5.0, 5.1, 5.4, 5.5, 5.9,
  ];
  values.forEach((a) => {
    values.forEach((b) => {
      const expected = Math.round(a) + Math.round(b);
      it(`${a} + ${b} = ${expected}`, () => {
        assert.strictEqual(calculateNumber(a, b), expected);
      });
    });
  });
});
