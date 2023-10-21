const vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];

function disemvowel(str) {
  str = str.replace(/[aeiou]/gi, "");
  return str;
  // for (let i = 0; i < str.length; i++) {
  //   if (vowel.includes(str[i])) {
  //     str = str.replace(str[i], "");
  //   }
  // }
  // return str;
}

console.log(
  disemvowel("No offense but,\nYour writing is among the worst I've ever read")
);
