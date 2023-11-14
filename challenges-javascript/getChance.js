function getChance(n, x, a) {
  if (x === a || x === 1) {
    return x / n;
  } else {
    return x > a ? (x - a) / n : (a - x) / n;
  }
}

console.log(getChance(100, 10, 10));
