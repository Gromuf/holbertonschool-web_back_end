export default function updateStudentGradeByCity(list, city, newGrades) {
  return list
    .filter((x) => x.location === city)
    .map((x) => {
      const gradeObj = newGrades.find((grade) => grade.studentId === x.id);
      return {
        ...x,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
