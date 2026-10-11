const { domesticQuote, internationalQuote } = require('./shipping');

const small = { weightKg: 2, lengthCm: 10, widthCm: 10, heightCm: 10, fragile: false };
const bulky = { weightKg: 1, lengthCm: 50, widthCm: 40, heightCm: 30, fragile: false };

describe('domesticQuote', () => {
  test('charges by actual weight when it exceeds volumetric weight', () => {
    expect(domesticQuote(small)).toBe(6.9);
  });

  test('charges by volumetric weight for bulky parcels', () => {
    expect(domesticQuote(bulky)).toBe(18.9);
  });

  test('adds a surcharge for fragile parcels', () => {
    expect(domesticQuote({ ...small, fragile: true })).toBe(9.9);
  });
});

describe('internationalQuote', () => {
  test('charges by actual weight when it exceeds volumetric weight', () => {
    expect(internationalQuote(small)).toBe(19.6);
  });

  test('charges by volumetric weight for bulky parcels', () => {
    expect(internationalQuote(bulky)).toBe(57.6);
  });

  test('adds a surcharge for fragile parcels', () => {
    expect(internationalQuote({ ...small, fragile: true })).toBe(22.6);
  });
});
