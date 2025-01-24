// 7-http_express.js

const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

function countStudents(databasePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(databasePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines
      const headers = lines.shift(); // Remove the header row

      const students = {};
      let totalStudents = 0;

      for (const line of lines) {
        const [firstname, lastname, age, field] = line.split(',');
        if (field) { // Ensure it's a valid student line
          if (!students[field.trim()]) {
            students[field.trim()] = [];
          }
          students[field.trim()].push(firstname.trim());
          totalStudents += 1;
        }
      }

      const summary = [];
      summary.push(`Number of students: ${totalStudents}`);
      Object.entries(students).forEach(([field, names]) => {
        summary.push(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
        );
      });

      resolve(summary.join('\n'));
    });
  });
}


app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const databasePath = process.argv[2];
  if (!databasePath) {
    res.status(500).send('Database file path must be provided');
    return;
  }
  try {
    const studentData = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentData}`);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;
