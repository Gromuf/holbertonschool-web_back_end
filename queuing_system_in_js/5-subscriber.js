// 5-subscriber.js
import redis from "redis";
const subscriber = redis.createClient();

subscriber.on("connect", () => {
  console.log("Redis client connected to the server");
});
subscriber.on("error", (err) => {
  console.log(`Redis Client not connected to the server: ${err.message}`, err);
});

subscriber.subscribe("holberton school channel");
subscriber.on("message", (channel, message) => {
  if (channel === "holberton school channel" && message === "KILL_SERVER") {
    subscriber.unsubscribe();
    subscriber.quit();
  } else {
    console.log(message);
  }
});
