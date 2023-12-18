const fs = require("fs");

//sort out the input file. I want an object with a game number, and then a list of winning numbers, and a list of numbers to check against
// {
//  cardNum: string
//  winningNums: array[...strings]
//  haveNums: array[...strings]
// }

const formattedInput = fs
  .readFileSync("input.txt", "utf-8")
  .split("\n")
  .map((line) => {
    const splitLine = line.split(/:\s|\s\|\s/);
    return {
      cardNum: splitLine[0].match(/(\d+)/g)[0],
      winningNums: splitLine[1].match(/(\d+)/g),
      haveNums: splitLine[2].match(/(\d+)/g),
    };
  });

//part1

//check how many winners exist in the haveNums. for the first winner, get one point. for subsequent winners, double the points (doubling sequence, get n matches and return 1 * 2^(n-1)?)

const part1 = formattedInput
  .map((game) => {
    let count = 0;

    game.haveNums.forEach((haveNum) => {
      game.winningNums.forEach((winningNum) => {
        if (haveNum === winningNum) count++;
      });
    });

    return Math.floor(Math.pow(2, count - 1)); //2^(n-1). rounded down because if the count is 0, end up with 2^(-1) which returns 0.5. this should remain 0. Bit of a cheat but whatever
  })
  .reduce((a, b) => a + b);

console.log(part1);

//part2

//make an empty array to add the number of duplicates to for each ticket (game)

const copies = Array(formattedInput.length).fill(1);

//loop through and add the required number of copies

for (let i = 0; i < formattedInput.length; i++) {
  let count = 0;

  formattedInput[i].haveNums.forEach((haveNum) => {
    formattedInput[i].winningNums.forEach((winningNum) => {
      if (haveNum === winningNum) count++;
    });
  });

  //add copies for copies

  for (let j = i + 1; j <= i + count; j++) {
    copies[j] += copies[i];
  }
}

//add it all up

const part2 = copies.reduce((a, b) => a + b);

console.log(part2);
