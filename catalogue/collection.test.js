const { Collection, ArchivedCatalogue } = require('./collection');

const books = [
  { id: 1, title: 'Middlemarch', year: 1871 },
  { id: 2, title: 'Beowulf', year: 1000 },
  { id: 3, title: 'Dune', year: 1965 },
];

describe('Collection', () => {
  test('adds and finds items by id', () => {
    const collection = new Collection();
    collection.add(books[0]);
    expect(collection.find(1)).toBe(books[0]);
  });

  test('removes items by id', () => {
    const collection = new Collection(books);
    collection.remove(2);
    expect(collection.count()).toBe(2);
    expect(collection.find(2)).toBeUndefined();
  });

  test('can be cleared', () => {
    const collection = new Collection(books);
    collection.clear();
    expect(collection.count()).toBe(0);
  });
});

describe('ArchivedCatalogue', () => {
  test('finds and counts archived items', () => {
    const archive = new ArchivedCatalogue(books);
    expect(archive.find(3).title).toBe('Dune');
    expect(archive.count()).toBe(3);
  });

  test('knows its oldest item', () => {
    expect(new ArchivedCatalogue(books).oldest().title).toBe('Beowulf');
  });

  test('cannot be changed', () => {
    const archive = new ArchivedCatalogue(books);
    expect(() => archive.add({ id: 4 })).toThrow();
    expect(() => archive.remove(1)).toThrow();
    expect(() => archive.clear()).toThrow();
    expect(archive.count()).toBe(3);
  });
});
