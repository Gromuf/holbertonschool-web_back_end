// 5-payment.test.js
const sinon = require("sinon");
const Utils = require("../utils");
const sendPaymentRequestToApi = require("../5-payment");
const expect = require("chai").expect;

describe("sendPaymentRequestToApi", function () {
  let spy;
  beforeEach(function () {
    spy = sinon.spy(console, "log");
  });
  afterEach(function () {
    spy.restore();
  });
  it("should log `The total is: 120` and be called once for (100, 20)", function () {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith("The total is: 120")).to.be.true;
  });
  it("should log `The total is: 20` and be called once for (10, 10)", function () {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith("The total is: 20")).to.be.true;
  });
});
