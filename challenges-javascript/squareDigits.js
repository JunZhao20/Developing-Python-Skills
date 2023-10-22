function squareDigits(num) {
  const str = num.toString();
  let result = "";
  for (let i = 0; i < str.length; i++) {
    result += Number(str[i]) ** 2;
  }
  return Number(result);
}

squareDigits(9119);
