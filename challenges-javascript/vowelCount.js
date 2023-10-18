const vowel = ["a", "e", "i", "o", "u"];

function getCount(str) {
  let count = 0;

  for (let i = 0; i < str.length; i++) {
    if (vowel.includes(str[i])) {
      count++;
    }
  }
  return count;
}

console.log(getCount("abracadabra"));
