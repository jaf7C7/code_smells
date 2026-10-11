class SeatMap {
  constructor(rows, seatsPerRow, accessibleSeats = []) {
    this.rows = rows;
    this.seatsPerRow = seatsPerRow;
    this.booked = new Set();
    this.accessible = new Set(accessibleSeats);
  }

  label(row, seat) {
    return `${String.fromCharCode(65 + row)}${seat}`;
  }

  allSeats() {
    const labels = [];
    for (let row = 0; row < this.rows; row++) {
      for (let seat = 1; seat <= this.seatsPerRow; seat++) {
        labels.push(this.label(row, seat));
      }
    }
    return labels;
  }

  book(label) {
    if (!this.allSeats().includes(label)) {
      throw new Error(`No seat ${label}`);
    }
    if (this.booked.has(label)) {
      return false;
    }
    this.booked.add(label);
    return true;
  }

  freeSeats() {
    return this.allSeats().filter((label) => !this.booked.has(label));
  }

  isAccessible(label) {
    return this.accessible.has(label);
  }
}

module.exports = { SeatMap };
