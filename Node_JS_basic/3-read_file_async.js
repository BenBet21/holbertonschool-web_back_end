const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter(line => line.trim() !== '');
        const students = lines.slice(1).map(line => {
          const [firstname, lastname, age, field] = line.split(',');
          return { firstname, lastname, age, field };
        });

        console.log(`Number of students: ${students.length}`);

        const fields = {};
        students.forEach(student => {
          if (!fields[student.field]) {
            fields[student.field] = [];
          }
          fields[student.field].push(student.firstname);
        });

        for (const [field, firstnames] of Object.entries(fields)) {
          console.log(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
        }

        resolve();
      }
    });
  });
}

module.exports = countStudents;