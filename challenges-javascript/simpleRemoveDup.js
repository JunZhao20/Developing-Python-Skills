function solve(arr) {
  // this converts the new set obejct into a list by using the spread op
  const dup = [...new Set(arr)];

  if (arr !== dup) {
    return dup;
  }
  return arr;
}

// console.log(solve([3, 4, 4, 3, 6, 3]));
// console.log(solve([3, 4, 6]));
console.log(solve([1, 2, 1, 2, 1, 2, 3]));
