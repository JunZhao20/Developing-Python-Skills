function spinWords(string) {
  const text = string.split(" ");
  let result = [];
  for (let x = 0; x < text.length; x++) {
    if (text[x].length >= 5) {
      const s = text[x].split("").reverse().join("");
      result.push(s);
    } else {
      result.push(text[x]);
    }
  }
  return result.join(" ");
}

console.log(spinWords("Hey fellow warriors"));
