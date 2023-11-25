function createPhoneNumber(numbers) {
  txt = numbers.join("");
  return `(${txt.slice(0, 3)}) ${txt.slice(3, 6)}-${txt.slice(6, 11)}`;
}

const show = createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);
console.log(show);
