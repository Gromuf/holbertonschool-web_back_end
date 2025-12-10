// 4-payment.test.js
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");
const expect = require("chai").expect;

describe("sendPaymentRequestToApi", function () {
  it("should stub Utils.calculateNumber and verify console.log output", function () {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const spy = sinon.spy(console, "log");
    sendPaymentRequestToApi(100, 20);
    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    expect(spy.calledWith("The total is: 10")).to.be.true;
    stub.restore();
    spy.restore();
  });
});
