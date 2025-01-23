// 3-read_file_async.js

const fs = require('fs').promises;

async function countStudent(path) {
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
    const totalStudents = Object.values(fieldCounts).reduce((sum, count) => sum + count, 0);
    console.log(`Number of studens: ${totalStudents}`);
    for (const [field, count] of Object.entries(fieldCounts)) {
      console.log(`Number of students in ${field}: ${count}. List: ${fieldStudents[field].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudent;
