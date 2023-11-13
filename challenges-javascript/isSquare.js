var isSquare = function (n) {
  if (Number.isInteger(Math.sqrt(n))) return true;
  return false;
};

console.log(isSquare(-1));
