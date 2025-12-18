import { expect } from "chai";
import sinon from "sinon";
import kue from "kue";
import createPushNotificationJobs from "./8-job.js";

describe("createPushNotificationJobs", () => {
  let queue;
  let consoleStub;

  before(() => {
    consoleStub = sinon.stub(console, "log");
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
    consoleStub.restore();
  });

  it("should throw an error if jobs is not an array", () => {
    expect(() => createPushNotificationJobs("not-an-array", queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("should create jobs in the queue", () => {
    const jobs = [
      { phoneNumber: "1234567890", message: "Test message 1" },
      { phoneNumber: "0987654321", message: "Test message 2" },
    ];

    createPushNotificationJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
