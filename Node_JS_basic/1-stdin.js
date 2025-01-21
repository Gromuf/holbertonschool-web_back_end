// 1-stdin.js
const readline = require("readline");

const interface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("Welcome to Holberton School, what is your name?");

interface.question("", (name) => {
  console.log(`Your name is: ${name}`);
  interface.close();
});

interface.on(`close`, () => {
  console.log("This important software is now closing");
  process.exit(0);
});
