export default function getStudentsByLocation(list, city) {
  return list.filter((x) => x.location === city);
}
