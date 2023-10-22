function highAndLow(numbers) {
  const lst = numbers.split(" ");
  let n = [];
  for (let i = 0; i < lst.length; i++) {
    n.push(Number(lst[i]));
  }
  return Math.max(...n), Math.min(...n);
}

console.log(highAndLow("1 2 3 4 5"));
