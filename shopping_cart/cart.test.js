const { Cart } = require('./cart');

test('cart', () => {
  const cart = new Cart();
  expect(cart.total()).toBe(0);

  cart.add('apple', 0.5, 3);
  expect(cart.quantityOf('apple')).toBe(3);
  expect(cart.total()).toBe(1.5);

  cart.add('apple', 0.5, 2);
  expect(cart.quantityOf('apple')).toBe(5);

  cart.add('bread', 1.2);
  expect(cart.quantityOf('bread')).toBe(1);
  expect(cart.total()).toBe(3.7);

  cart.remove('apple', 2);
  expect(cart.quantityOf('apple')).toBe(3);

  cart.remove('bread');
  expect(cart.quantityOf('bread')).toBe(0);
  expect(() => cart.remove('bread')).toThrow('bread is not in the cart');

  cart.applyCoupon('TENOFF');
  expect(cart.total()).toBe(1.35);
  expect(() => cart.applyCoupon('BOGUS')).toThrow('Unknown coupon: BOGUS');

  cart.clear();
  expect(cart.quantityOf('apple')).toBe(0);
  cart.add('pear', 2);
  expect(cart.total()).toBe(2);
});
