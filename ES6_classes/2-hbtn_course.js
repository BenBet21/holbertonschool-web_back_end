export default class HolbertonCourse {
  constructor(name, lenght, students) {
    this._name = name;
    this._length = lenght;
    this._students = students;
  }

  get name() {
    return this._name;
  }
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('name must be a string');
    } 
    this._name = value;
  }

  get lenght() {
    return this._lenght;
  }
  set lenght(value) {
    if (typeof value !== 'number') {
      throw new TypeError('name must be a number');
    } 
    this._lenght = value;
  }

  get students() {
    return this._students;
  }
  set students(value) {
    for (value in students) {
      if (typeof value !== 'string') {
        throw new TypeError('students must be an array of strings');
      } 
      this._students = value;
    }
  }
}
