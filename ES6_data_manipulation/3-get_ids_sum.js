/* eslint-disable */
import getListStudents from "./0-get_list_students";

export default function getStudentIdsSum() {
  const studentsId = getListStudents();
  return studentsId.reduce((sum, student) => sum + student.id, 0);
  }
