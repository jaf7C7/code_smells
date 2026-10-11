const { bookTickets } = require('./tickets');

describe('bookTickets', () => {
  test('charges the section price for each ticket', () => {
    const booking = bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 2, 'stalls', false, null);
    expect(booking.total).toBe(90);
  });

  test('applies a promo code discount', () => {
    const booking = bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 2, 'stalls', false, 'EARLYBIRD');
    expect(booking.total).toBe(81);
  });

  test('ignores unknown promo codes', () => {
    const booking = bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 2, 'stalls', false, 'BOGUS');
    expect(booking.total).toBe(90);
  });

  test('adds insurance per ticket', () => {
    const booking = bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 2, 'stalls', true, null);
    expect(booking.total).toBe(95);
  });

  test('allows up to eight tickets', () => {
    const booking = bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 8, 'balcony', false, null);
    expect(booking.total).toBe(160);
  });

  test('rejects more than eight tickets', () => {
    expect(() => bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 9, 'stalls', false, null)).toThrow();
  });

  test('rejects unknown sections', () => {
    expect(() => bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 1, 'roof', false, null)).toThrow();
  });

  test('describes the booking in the confirmation', () => {
    const booking = bookTickets('Hamlet', '2025-03-01', 'The Globe', 'Ada', 'ada@example.com', 2, 'circle', false, null);
    expect(booking.confirmation).toBe('Ada <ada@example.com>: 2 x circle for Hamlet at The Globe on 2025-03-01');
  });
});
