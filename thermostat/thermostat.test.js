const { action, scheduledTarget } = require('./thermostat');

describe('action', () => {
  test('heats when the room is colder than the target', () => {
    expect(action(18, 20, 'heat')).toBe('heating');
  });

  test('heats when more than half a degree below the target', () => {
    expect(action(19.4, 20, 'heat')).toBe('heating');
  });

  test('does not heat when within half a degree of the target', () => {
    expect(action(19.5, 20, 'heat')).toBe('idle');
  });

  test('cools when the room is warmer than the target', () => {
    expect(action(25, 22, 'cool')).toBe('cooling');
  });

  test('does not cool when within half a degree of the target', () => {
    expect(action(22.5, 22, 'cool')).toBe('idle');
  });

  test('does nothing when switched off', () => {
    expect(action(10, 20, 'off')).toBe('idle');
  });

  test('rejects unknown modes', () => {
    expect(() => action(18, 20, 'turbo')).toThrow('Unknown mode: turbo');
  });
});

describe('scheduledTarget', () => {
  test('is 20 degrees during the day', () => {
    expect(scheduledTarget(7)).toBe(20);
    expect(scheduledTarget(21)).toBe(20);
  });

  test('is 16 degrees at night', () => {
    expect(scheduledTarget(22)).toBe(16);
    expect(scheduledTarget(6)).toBe(16);
  });
});
