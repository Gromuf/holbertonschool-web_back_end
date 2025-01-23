// 5-http.js

const http = require('http');
const fs = require('fs').promises;

async function readStudentData(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    if (lines.length < 2) {
      throw new Error('No valid student data found in the file');
    }
    const headers = lines[0].split(',');
    const students = lines.slice(1);
    const fieldCounts = {};
    const fieldStudents = {};
    for (const student of students) {
      const values = student.split(',');
      if (values.length === headers.length) {
        const field = values[values.length - 1].trim();
        const firstName = values[0].trim();
        if (!fieldCounts[field]) {
          fieldCounts[field] = 0;
          fieldStudents[field] = [];
        }
        fieldCounts[field] += 1;
        fieldStudents[field].push(firstName);
      }
    }
    return { fieldCounts, fieldStudents };
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databasePath = req.url.split('?')[1];
    if (!databasePath) {
      res.statusCode = 400;
      res.end('Database file path missing');
      return;
    }
    try {
      const { fieldCounts, fieldStudents } = await readStudentData(databasePath);
      let response = 'This is the list of our students \n';
      for (const [field, count] of Object.entries(fieldCounts)) {
        response += `Number of students in ${field}: ${count}. List: ${fieldStudents[field].join(', ')}\n`;
      }
      res.end(response);
    } catch (error) {
      res.statusCode = 500;
      res.end('Cannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});
app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});
module.exports = app;
