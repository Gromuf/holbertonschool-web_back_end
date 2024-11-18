export default function getStudentIdsSum(list) {
  return list.reduce((a, b) => a + b.id, 0);
}
