// 6-payment_token.test.js
const getPaymentTokenFromAPI = require("./6-payment_token");
const expect = require("chai").expect;
describe("getPaymentTokenFromAPI", function () {
  it("should return a resolved promise with the correct data when called with true", function () {
    return getPaymentTokenFromAPI(true).then((response) => {
      expect(response).to.deep.equal({
        data: "Successful response from the API",
      });
    });
  });
  it("should throw an error when called with false", function () {
    expect(() => getPaymentTokenFromAPI(false)).to.throw("API request failed");
  });
});
