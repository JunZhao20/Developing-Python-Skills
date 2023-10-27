function solution(number) {
  let num = 0;
  let lst = [];
  let sum = 0;
  for (let i = 0; i < number; i++) {
    lst.push(num++);
  }

  for (let x = 0; x < lst.length; x++) {
    if (lst[x] % 3 == 0 || lst[x] % 5 == 0) {
      sum += lst[x];
    }
  }
  return sum;
}

//   for (let x = 0; x < lst.length; x++)
//     if (lst[x] >= -1) {
//       const calc = lst.filter((n) => {
//         if (n % 3 == 0 || n % 5 == 0) {
//           return n;
//         }
//       });
//       // through each iteration it will add up within the accumulator
//       const sum = calc.reduce((accumulator, currentValue) => {
//         // this makes sue the currentValue is added up accumulator
//         return accumulator + currentValue, 0;
//       });
//       return sum;
//     }
//   return 0;
// }
console.log(solution(10));
