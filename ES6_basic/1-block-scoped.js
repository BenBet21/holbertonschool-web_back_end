export default function taskBlock(trueOrFalse) {
  const task = trueOrFalse ? true : false;
  const task2 = !task;

  return [task, task2];
}
