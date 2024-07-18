import Classroom from './0-classroom';

function initializeRooms() {
  
    const room1 = new Classroom(19);
    const room2 = new Classroom(20);
    const room3 = new Classroom(34);
  
    return [room1, room2, room3];
}
