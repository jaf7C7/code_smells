function normalise(part) {
  return part.trim().toLowerCase().replace(/\s+/g, ' ');
}

function addressKey(street, city, postcode) {
  return [street, city, postcode].map(normalise).join('|');
}

function formatLabel(recipient, street, city, postcode) {
  return [recipient, street, `${city} ${postcode.toUpperCase()}`].join('\n');
}

function deliveryLabel(order) {
  return formatLabel(order.recipient, order.deliveryStreet, order.deliveryCity, order.deliveryPostcode);
}

function invoiceLabel(order) {
  return formatLabel(order.recipient, order.billingStreet, order.billingCity, order.billingPostcode);
}

function needsSeparateInvoice(order) {
  return (
    addressKey(order.billingStreet, order.billingCity, order.billingPostcode) !==
    addressKey(order.deliveryStreet, order.deliveryCity, order.deliveryPostcode)
  );
}

module.exports = { deliveryLabel, invoiceLabel, needsSeparateInvoice };
