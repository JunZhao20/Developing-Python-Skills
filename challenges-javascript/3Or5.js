function solution(number) {
  let num = 0;
  let lst = [];
  for (let i = 0; i < number; i++) {
    lst.push(num++);
  }

  for (let x = 0; x < lst.length; x++)
    if (lst[x] >= -1) {
      const calc = lst.filter((n) => {
        if (n % 3 == 0 || n % 5 == 0) {
          return n;
        }
      });
      // through each iteration it will add up within the accumulator
      const sum = calc.reduce((accumulator, currentValue) => {
        // this makes sue the currentValue is added up accumulator
        return accumulator + currentValue;
      });
      return sum;
    }
  return 0;
}
console.log(solution(1));
