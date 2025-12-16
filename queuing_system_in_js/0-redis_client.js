// 0-redis_client.js
import { createClient } from "redis";

const redisClient = createClient({ url: "redis://localhost:6379" });

redisClient.on("connect", () => {
  console.log("Redis client connected to the server");
});
redisClient.on("error", (err) => {
  console.log(`Redis Client not connected to the server: ${err.message}`, err);
});

export default redisClient;
