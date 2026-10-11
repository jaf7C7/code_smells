class Collection {
  constructor(items = []) {
    this.items = [...items];
  }

  add(item) {
    this.items.push(item);
  }

  remove(id) {
    this.items = this.items.filter((item) => item.id !== id);
  }

  clear() {
    this.items = [];
  }

  find(id) {
    return this.items.find((item) => item.id === id);
  }

  count() {
    return this.items.length;
  }
}

class ArchivedCatalogue extends Collection {
  add() {
    throw new Error('The archive cannot be changed');
  }

  remove() {
    throw new Error('The archive cannot be changed');
  }

  clear() {
    throw new Error('The archive cannot be changed');
  }

  oldest() {
    return this.items.reduce((oldest, item) => (item.year < oldest.year ? item : oldest));
  }
}

module.exports = { Collection, ArchivedCatalogue };
