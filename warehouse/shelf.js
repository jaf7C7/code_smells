class Shelf {
  constructor(id, capacity) {
    this._id = id;
    this._capacity = capacity;
    this._items = new Map();
  }

  get id() {
    return this._id;
  }
}

module.exports = { Shelf };
