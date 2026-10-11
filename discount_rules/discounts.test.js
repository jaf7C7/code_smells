const { discountFor, priceFor } = require('./discounts');

describe('discountFor', () => {
  test('gives 20% off in the customer\'s birthday month', () => {
    expect(discountFor({ birthMonth: 6, member: false })).toBe(0.2);
  });

  test('gives members 10% off at weekends', () => {
    expect(discountFor({ birthMonth: 1, member: true })).toBe(0.1);
  });

  test('gives non-members no discount outside their birthday month', () => {
    expect(discountFor({ birthMonth: 1, member: false })).toBe(0);
  });
});

describe('priceFor', () => {
  test('applies the discount to the price', () => {
    expect(priceFor({ birthMonth: 6, member: true }, 49.99)).toBe(39.99);
  });
});
