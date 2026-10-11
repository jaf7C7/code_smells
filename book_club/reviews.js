function averageRating(reviews, title) {
  let total = 0;
  let count = 0;
  for (const review of reviews) {
    if (review.title === title) {
      total += review.stars;
      count += 1;
    }
  }
  return count === 0 ? null : total / count;
}

function activeReviewers(reviews, minimumReviews) {
  const counts = {};
  for (const review of reviews) {
    counts[review.reviewer] = (counts[review.reviewer] || 0) + 1;
  }
  const result = [];
  for (const reviewer of Object.keys(counts)) {
    if (counts[reviewer] >= minimumReviews) {
      result.push(reviewer);
    }
  }
  result.sort();
  return result;
}

function titlesRatedAtLeast(reviews, stars) {
  const titles = [];
  for (let i = 0; i < reviews.length; i++) {
    if (reviews[i].stars >= stars && !titles.includes(reviews[i].title)) {
      titles.push(reviews[i].title);
    }
  }
  return titles;
}

module.exports = { averageRating, activeReviewers, titlesRatedAtLeast };
