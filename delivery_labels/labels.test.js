const { deliveryLabel, invoiceLabel, needsSeparateInvoice } = require('./labels');

function order(overrides = {}) {
  return {
    recipient: 'Ada Lovelace',
    deliveryStreet: '12 St James Square',
    deliveryCity: 'London',
    deliveryPostcode: 'sw1y 4jh',
    billingStreet: '12 St James Square',
    billingCity: 'London',
    billingPostcode: 'sw1y 4jh',
    ...overrides,
  };
}

describe('deliveryLabel', () => {
  test('puts recipient, street and town on separate lines', () => {
    expect(deliveryLabel(order())).toBe('Ada Lovelace\n12 St James Square\nLondon SW1Y 4JH');
  });
});

describe('invoiceLabel', () => {
  test('uses the billing address', () => {
    const label = invoiceLabel(order({ billingStreet: '1 Main Street', billingCity: 'Leeds', billingPostcode: 'ls1 1aa' }));
    expect(label).toBe('Ada Lovelace\n1 Main Street\nLeeds LS1 1AA');
  });
});

describe('needsSeparateInvoice', () => {
  test('is false when billing and delivery addresses match', () => {
    expect(needsSeparateInvoice(order())).toBe(false);
  });

  test('ignores differences in case and spacing', () => {
    expect(needsSeparateInvoice(order({ billingStreet: '12  st james square ', billingPostcode: 'SW1Y 4JH' }))).toBe(false);
  });

  test('is true when the addresses differ', () => {
    expect(needsSeparateInvoice(order({ billingCity: 'Leeds' }))).toBe(true);
  });
});
