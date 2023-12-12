const fs = require("fs");

const formattedInput = fs.readFileSync("input.txt", "utf-8").split("\n");

//part 1

let part1 = 0;
let part2 = 0;

formattedInput.forEach((line, i) => {
  const nums = line.replaceAll(/\./g, " ").matchAll(/\d+/g); //makes iterable object (NOT array (I didn't know that)), hence the lack of forEach/for...in on line 12)

  for (const match of nums) {
    for (j = match.index; j < match.index + match[0].length; j++) {
      const nextDoor = [
        //check line and row ahead and behind to include diagonals. also learnt nullish coalescing operator ?? https://www.scaler.com/topics/javascript-nullish-coalescing-operator/
        (formattedInput[i - 1] ?? "")[j - 1] ?? ".",
        (formattedInput[i] ?? "")[j - 1] ?? ".",
        (formattedInput[i + 1] ?? "")[j - 1] ?? ".",
        (formattedInput[i - 1] ?? "")[j] ?? ".",
        (formattedInput[i] ?? "")[j] ?? ".",
        (formattedInput[i + 1] ?? "")[j] ?? ".",
        (formattedInput[i - 1] ?? "")[j + 1] ?? ".",
        (formattedInput[i] ?? "")[j + 1] ?? ".",
        (formattedInput[i + 1] ?? "")[j + 1] ?? ".",
      ];

      if (nextDoor.some((x) => /[^0-9.]/.test(x))) {
        part1 += parseInt(match[0]);
        //stuck for ages here. realised numbers could be added twice here so added break line to stop working on the current "j" of "match" if it's already been added
        break;
      }
    }
  }
});

console.log(part1);

//part 2
