function highestRank(arr) {
  //Your Code logic should written here
  const dict = {};
  // iterate over each elem in arr
  arr.forEach((i) => {
    //   assigning each dict key value with counter
    dict[i] = (dict[i] || 0) + 1; // use ternary operator to check if each dict key has value assigned to it.
  });
  const val = Object.values(dict);
  // sort to find max num
  const sorted = val.sort();
  console.log(sorted);
  // grabs list of keys, looks for each key that has the highest value by comparing each key to the highest sorted value in sorted list
  return Number(
    Object.keys(dict).find((key) => dict[key] === sorted[sorted.length - 1])
  );

  // for (let x = 0; x < dict.length; x++) { }
}

const res = highestRank([
  6, 13, 16, 18, 18, 11, 18, 15, 27, 24, 24, 17, 17, 17, 9, 11, 5, 11, 7, 13,
  12,
]);
console.log(res);
