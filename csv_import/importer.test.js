const { Importer } = require('./importer');

const csv = `
name, quantity, price
apple, 3, 0.5
pear, 2, 0.75
`;

function imported() {
  const importer = new Importer();
  importer.load(csv);
  importer.readHeader();
  return importer;
}

describe('Importer', () => {
  test('turns each line into a record keyed by column name', () => {
    expect(imported().rows()).toEqual([
      { name: 'apple', quantity: '3', price: '0.5' },
      { name: 'pear', quantity: '2', price: '0.75' },
    ]);
  });

  test('totals a numeric column', () => {
    expect(imported().total('quantity')).toBe(5);
  });

  test('reads the column names from the header line', () => {
    expect(imported().columns).toEqual(['name', 'quantity', 'price']);
  });
});
