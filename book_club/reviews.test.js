const { averageRating, activeReviewers, titlesRatedAtLeast } = require('./reviews');

const reviews = [
  { reviewer: 'sam', title: 'Middlemarch', stars: 5 },
  { reviewer: 'ali', title: 'Middlemarch', stars: 3 },
  { reviewer: 'sam', title: 'Dune', stars: 4 },
  { reviewer: 'kim', title: 'Dune', stars: 2 },
  { reviewer: 'ali', title: 'Beloved', stars: 4 },
  { reviewer: 'sam', title: 'Beloved', stars: 5 },
];

describe('averageRating', () => {
  test('averages the stars given to a title', () => {
    expect(averageRating(reviews, 'Middlemarch')).toBe(4);
  });

  test('is null for a title nobody has reviewed', () => {
    expect(averageRating(reviews, 'Ulysses')).toBeNull();
  });
});

describe('activeReviewers', () => {
  test('lists reviewers with at least the given number of reviews, alphabetically', () => {
    expect(activeReviewers(reviews, 2)).toEqual(['ali', 'sam']);
  });

  test('includes everyone when the minimum is one', () => {
    expect(activeReviewers(reviews, 1)).toEqual(['ali', 'kim', 'sam']);
  });
});

describe('titlesRatedAtLeast', () => {
  test('lists each title with a rating at or above the given stars once', () => {
    expect(titlesRatedAtLeast(reviews, 4)).toEqual(['Middlemarch', 'Dune', 'Beloved']);
  });

  test('excludes titles whose ratings are all lower', () => {
    expect(titlesRatedAtLeast(reviews, 5)).toEqual(['Middlemarch', 'Beloved']);
  });
});
