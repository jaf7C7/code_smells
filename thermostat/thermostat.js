const MODES = ['heat', 'cool', 'off'];
const HYSTERESIS = 0.5;
const MAX_TARGET = 30;

function celsiusToFahrenheit(celsius) {
  return (celsius * 9) / 5 + 32;
}

function action(current, target, mode) {
  if (!MODES.includes(mode)) {
    throw new Error(`Unknown mode: ${mode}`);
  }
  if (mode === 'off') {
    return 'idle';
  }
  if (mode === 'heat') {
    return current < target - HYSTERESIS ? 'heating' : 'idle';
  }
  if (mode === 'cool') {
    return current > target + HYSTERESIS ? 'cooling' : 'idle';
  }
  if (mode === 'eco') {
    return current < target - 2 ? 'heating' : 'idle';
  }
  return 'idle';
}

function scheduledTarget(hour) {
  if (hour >= 7 && hour < 22) {
    return 20;
  }
  return 16;
}

module.exports = { action, scheduledTarget };
