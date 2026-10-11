function roundQuantity(quantity) {
  return quantity >= 10 ? Math.round(quantity) : Math.round(quantity * 10) / 10;
}

function scale(recipe, servings) {
  const factor = servings / recipe.serves;
  return {
    ...recipe,
    serves: servings,
    ingredients: recipe.ingredients.map((ingredient) => ({
      ...ingredient,
      quantity: roundQuantity(ingredient.quantity * factor),
    })),
  };
}

function shoppingList(recipes) {
  const totals = new Map();
  for (const recipe of recipes) {
    for (const { name, quantity, unit } of recipe.ingredients) {
      const key = `${name} (${unit})`;
      totals.set(key, (totals.get(key) || 0) + quantity);
    }
  }
  return [...totals.entries()].sort(([a], [b]) => a.localeCompare(b)).map(([key, quantity]) => `${key}: ${quantity}`);
}

module.exports = { scale, shoppingList };
