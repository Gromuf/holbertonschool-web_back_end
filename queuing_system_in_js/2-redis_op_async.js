// 2-redis_op_async.js
import redis from "redis";
import { promisify } from "util";

const redisClient = redis.createClient();

redisClient.on("connect", () => {
  console.log("Redis client connected to the server");
});
redisClient.on("error", (err) => {
  console.log(`Redis Client not connected to the server: ${err.message}`, err);
});

function setNewSchool(schoolName, value) {
  redisClient.SET(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  const getAsync = promisify(redisClient.get).bind(redisClient);
  getAsync(schoolName)
    .then((reply) => {
      console.log(reply);
    })
    .catch((err) => {
      console.log(err);
    });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
