function findOdd(A) {
  // expand values in set obj into a list
  const find = {};
  A.forEach((x) => {
    find[x] = (find[x] || 0) + 1;
  });

  for (const key in find) {
    if (find[key] % 2 !== 0) {
      return parseInt(key);
    }
  }
}

console.log(findOdd([1, 1, 2]));
