const COUPONS = { TENOFF: 0.1, HALFPRICE: 0.5 };

class Cart {
  constructor() {
    this.lines = new Map();
    this.discount = 0;
  }

  add(name, unitPrice, quantity = 1) {
    const line = this.lines.get(name);
    if (line) {
      line.quantity += quantity;
    } else {
      this.lines.set(name, { unitPrice, quantity });
    }
  }

  remove(name, quantity = 1) {
    const line = this.lines.get(name);
    if (!line) {
      throw new Error(`${name} is not in the cart`);
    }
    line.quantity -= quantity;
    if (line.quantity <= 0) {
      this.lines.delete(name);
    }
  }

  quantityOf(name) {
    return this.lines.get(name)?.quantity ?? 0;
  }

  applyCoupon(code) {
    if (!(code in COUPONS)) {
      throw new Error(`Unknown coupon: ${code}`);
    }
    this.discount = COUPONS[code];
  }

  total() {
    const subtotal = [...this.lines.values()].reduce((sum, line) => sum + line.unitPrice * line.quantity, 0);
    return Math.round(subtotal * (1 - this.discount) * 100) / 100;
  }

  clear() {
    this.lines.clear();
    this.discount = 0;
  }
}

module.exports = { Cart };
