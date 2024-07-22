/* eslint-disable */
import getListStudents from "./0-get_list_students";

export default function getStudentsByLocation(arrayOfStudents, city) {
  if (!Array.isArray(arrayOfStudents)) {
    return [];
  }
  return arrayOfStudents.filter(student => student.location === city);
  }
