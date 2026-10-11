class Picker {
  pick(shelf, sku, quantity) {
    const available = shelf._items.get(sku) || 0;
    if (available < quantity) {
      throw new Error(`Only ${available} of ${sku} on shelf ${shelf.id}`);
    }
    if (available === quantity) {
      shelf._items.delete(sku);
    } else {
      shelf._items.set(sku, available - quantity);
    }
  }
}

class Restocker {
  restock(shelf, sku, quantity) {
    let used = 0;
    shelf._items.forEach((count) => {
      used += count;
    });
    if (used + quantity > shelf._capacity) {
      throw new Error(`Shelf ${shelf.id} has room for ${shelf._capacity - used} more`);
    }
    shelf._items.set(sku, (shelf._items.get(sku) || 0) + quantity);
  }
}

function stockReport(shelf) {
  return [...shelf._items.entries()].map(([sku, count]) => `${sku}: ${count}`).sort();
}

module.exports = { Picker, Restocker, stockReport };
