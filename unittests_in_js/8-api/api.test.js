// api.test.js
const request = require("request");
const { expect } = require("chai");

describe("Index page", () => {
  const url = "http://localhost:7865";
  it("should return status code 200", (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("should return the correct welcome message", (done) => {
    request.get(url, (error, response, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
  it("should not return an error", (done) => {
    request.get(url, (error, response, body) => {
      expect(error).to.be.null;
      done();
    });
  });
});
