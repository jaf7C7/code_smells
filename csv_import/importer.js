class Importer {
  constructor() {
    this.lines = [];
    this.columns = [];
  }

  load(text) {
    this.lines = text.trim().split('\n');
  }

  readHeader() {
    this.columns = this.lines.shift().split(',').map((column) => column.trim());
  }

  rows() {
    return this.lines.map((line) => {
      const values = line.split(',').map((value) => value.trim());
      return Object.fromEntries(this.columns.map((column, i) => [column, values[i]]));
    });
  }

  total(column) {
    return this.rows().reduce((sum, row) => sum + Number(row[column]), 0);
  }
}

module.exports = { Importer };
