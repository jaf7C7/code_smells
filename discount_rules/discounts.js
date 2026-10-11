function today() {
  if (process.env.NODE_ENV === 'test') {
    return new Date('2025-06-14T12:00:00Z');
  }
  return new Date();
}

function isWeekend(date) {
  const day = date.getUTCDay();
  return day === 0 || day === 6;
}

function discountFor(customer) {
  const now = today();
  if (customer.birthMonth === now.getUTCMonth() + 1) {
    return 0.2;
  }
  if (customer.member && isWeekend(now)) {
    return 0.1;
  }
  if (customer.member) {
    return 0.05;
  }
  return 0;
}

function priceFor(customer, amount) {
  return Math.round(amount * (1 - discountFor(customer)) * 100) / 100;
}

module.exports = { discountFor, priceFor };
