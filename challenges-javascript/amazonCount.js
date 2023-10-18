function countArara(n) {
  const Num = {
    1: "anane",
    2: "adak ",
  };

  const n1 = n / 2;
  if (n % 2 === 0) {
    return Num["2"].repeat(n1).trim();
  } else {
    const n2 = Math.floor(n1);
    return (Num["2"].repeat(n2) + Num["1"].repeat(1)).trim();
  }
}

console.log(countArara(1));
