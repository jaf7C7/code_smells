const SECTION_PRICES = { stalls: 45, circle: 35, balcony: 20 };
const PROMO_DISCOUNTS = { EARLYBIRD: 0.1, FRIENDS: 0.15 };

function bookTickets(eventName, eventDate, venue, customerName, customerEmail, quantity, section, insured, promoCode) {
  if (quantity < 1 || quantity > 8) {
    throw new Error('You can book between 1 and 8 tickets');
  }
  const unitPrice = SECTION_PRICES[section];
  if (unitPrice === undefined) {
    throw new Error(`Unknown section: ${section}`);
  }
  const discount = PROMO_DISCOUNTS[promoCode] ?? 0;
  const ticketsTotal = unitPrice * quantity * (1 - discount);
  const insuranceTotal = insured ? 2.5 * quantity : 0;
  return {
    confirmation: `${customerName} <${customerEmail}>: ${quantity} x ${section} for ${eventName} at ${venue} on ${eventDate}`,
    total: Math.round((ticketsTotal + insuranceTotal) * 100) / 100,
  };
}

module.exports = { bookTickets };
