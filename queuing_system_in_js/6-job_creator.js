// 6-job_creator.js
import Kue from 'kue';
const queue = Kue.createQueue();

const jobData = {
  phoneNumber: String,
  message: String,
}

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err){
	console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log(`Notification job ${job.id} completed`);
}).on('failed', (err) => {
  console.log(`Notification job ${job.id} failed: ${err}`);
})
