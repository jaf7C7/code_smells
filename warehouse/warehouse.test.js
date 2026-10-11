const { Shelf } = require('./shelf');
const { Picker, Restocker, stockReport } = require('./staff');

function stockedShelf() {
  const shelf = new Shelf('A1', 10);
  new Restocker().restock(shelf, 'bolt', 4);
  new Restocker().restock(shelf, 'nut', 3);
  return shelf;
}

describe('warehouse', () => {
  test('reports what is on a shelf', () => {
    expect(stockReport(stockedShelf())).toEqual(['bolt: 4', 'nut: 3']);
  });

  test('restocking adds to what is already there', () => {
    const shelf = stockedShelf();
    new Restocker().restock(shelf, 'bolt', 2);
    expect(stockReport(shelf)).toEqual(['bolt: 6', 'nut: 3']);
  });

  test('restocking can fill a shelf exactly', () => {
    const shelf = stockedShelf();
    new Restocker().restock(shelf, 'washer', 3);
    expect(stockReport(shelf)).toContain('washer: 3');
  });

  test('restocking refuses to overfill a shelf', () => {
    expect(() => new Restocker().restock(stockedShelf(), 'washer', 4)).toThrow('Shelf A1 has room for 3 more');
  });

  test('picking takes items off the shelf', () => {
    const shelf = stockedShelf();
    new Picker().pick(shelf, 'bolt', 1);
    expect(stockReport(shelf)).toEqual(['bolt: 3', 'nut: 3']);
  });

  test('picking the last items removes them from the report', () => {
    const shelf = stockedShelf();
    new Picker().pick(shelf, 'nut', 3);
    expect(stockReport(shelf)).toEqual(['bolt: 4']);
  });

  test('cannot pick more than is on the shelf', () => {
    expect(() => new Picker().pick(stockedShelf(), 'nut', 4)).toThrow('Only 3 of nut on shelf A1');
  });
});
