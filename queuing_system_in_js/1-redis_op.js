// 1-redis_op.js
import redis from "redis";

const redisClient = redis.createClient();

redisClient.on("connect", () => {
  console.log("Redis client connected to the server");
});
redisClient.on("error", (err) => {
  console.log(`Redis Client not connected to the server: ${err.message}`, err);
});

export default redisClient;

function setNewSchool(schoolName, value) {
  redisClient.SET(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(reply);
  });
}

export { setNewSchool, displaySchoolValue };

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
