function highAndLow(numbers) {
  const lst = numbers.split(" ");
  let n = [];
  for (let i = 0; i < lst.length; i++) {
    n.push(Number(lst[i]));
  }
  let min = Math.min(...n);
  let max = Math.max(...n);
  return `${max} ${min}`;
}

console.log(highAndLow("1 2 3 4 5"));
