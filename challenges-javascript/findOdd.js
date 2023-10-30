function findOdd(A) {
  // expand values in set obj into a list
  let count = 0;
  const u = [...new Set(A)];
  const obj = new Set(A);
  console.log(obj);
  for (let i = 0; i < u.length; i++) {
    let n = u[i];
    if (u.includes(n)) {
      obj(count++;
    }
    console.log(obj);
  }
}

console.log(findOdd([1, 1, 2]));
