/* eslint-disable */

export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number')
      throw new TypeError ('size must be a number')
    if (typeof location !== 'string')
      throw new TypeError !== ('location must be a string')
    this._size = size;
    this._code = code;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof value !== 'number')
      throw new TypeError ('size must be a number');
    this._name = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    if (typeof value !== 'string')
      throw new TypeError ('location must be a string');
    this._location = value;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }






}