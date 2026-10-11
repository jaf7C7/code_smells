const { SeatMap } = require('./seats');

describe('SeatMap', () => {
  test('labels seats by row letter and seat number', () => {
    const map = new SeatMap(3, 4);
    for (let row = 0; row < 3; row++) {
      for (let seat = 1; seat <= 4; seat++) {
        if (row === 0) {
          expect(map.label(row, seat)).toBe(`A${seat}`);
        } else if (row === 1) {
          expect(map.label(row, seat)).toBe(`B${seat}`);
        } else {
          expect(map.label(row, seat)).toBe(`C${seat}`);
        }
      }
    }
  });

  test('booked seats are no longer free', () => {
    const map = new SeatMap(2, 2);
    map.book('A2');
    const free = map.freeSeats();
    for (const label of ['A1', 'A2', 'B1', 'B2']) {
      if (label === 'A2') {
        expect(free).not.toContain(label);
      } else {
        expect(free).toContain(label);
      }
    }
  });

  test('a seat cannot be booked twice', () => {
    const map = new SeatMap(2, 2);
    map.book('A1');
    const result = map.book('A1');
    if (result === false) {
      expect(map.freeSeats()).toEqual(['A2', 'B1', 'B2']);
    } else {
      throw new Error('double booking was allowed');
    }
  });

  test('knows which seats are accessible', () => {
    const map = new SeatMap(2, 4, ['A1', 'A4']);
    for (const label of map.freeSeats()) {
      if (label === 'A1' || label === 'A4') {
        expect(map.isAccessible(label)).toBe(true);
      } else {
        expect(map.isAccessible(label)).toBe(false);
      }
    }
  });

  test('refuses seats that do not exist', () => {
    const map = new SeatMap(2, 2);
    try {
      map.book('C1');
    } catch (error) {
      expect(error.message).toBe('No seat C1');
    }
  });
});
