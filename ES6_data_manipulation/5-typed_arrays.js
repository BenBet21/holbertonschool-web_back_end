/* eslint-disable */
export default function createInt8TypedArray(length, position, value) {
  if (typeof length !== 'number' || typeof position !== 'number' || typeof value !== 'number')
    throw new TypeError('Arguments must be a number');
  const buffer = new ArrayBuffer(length);
  const Dataview = new DataView(buffer);
  if (position < 0 || position >= length) throw new Error('Position outside range');
  Dataview.setInt8(position, value);
  return Dataview;
}
