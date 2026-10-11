const fs = require('fs');
const path = require('path');
const { scale, shoppingList } = require('./scaler');

const recipes = JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures', 'recipes.json'), 'utf8'));

describe('scale', () => {
  test('scales a recipe up', () => {
    expect(scale(recipes[2], 6).ingredients[1].quantity).toBe(450);
  });

  test('scales a recipe down', () => {
    expect(scale(recipes[3], 4).ingredients[1].quantity).toBe(2.7);
  });

  test('rounds small quantities to one decimal place', () => {
    expect(scale(recipes[2], 3).ingredients[2].quantity).toBe(0.8);
  });

  test('rounds large quantities to whole numbers', () => {
    expect(scale(recipes[3], 5).ingredients[0].quantity).toBe(117);
  });

  test('records the new number of servings', () => {
    expect(scale(recipes[1], 3).serves).toBe(3);
  });
});

describe('shoppingList', () => {
  test('combines ingredients across recipes', () => {
    expect(shoppingList([recipes[0], recipes[1]])).toContain('egg (whole): 5');
  });

  test('lists every ingredient once, alphabetically', () => {
    expect(shoppingList([recipes[0], recipes[2]])).toHaveLength(5);
    expect(shoppingList([recipes[0], recipes[2]])[0]).toBe('egg (whole): 2');
  });
});
