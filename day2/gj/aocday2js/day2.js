const fs = require("node:fs");

const formattedInput = fs
  .readFileSync("input.txt", "utf-8")
  .split("\n")
  .map((line) => line.split(/:\s|;\s/))
  .map((line) => {
    const gameNum = line.shift().slice(5);
    const draws = [
      ...line.map((draws) =>
        draws.split(/, /).map((draw) => {
          const num = parseInt(draw.split(" ")[0]);
          const colour = draw.split(" ")[1];
          return {
            num,
            colour,
          };
        })
      ),
    ].map((draw) => {
      return {
        green: (draw.find((item) => item.colour === "green") ?? 0).num ?? 0,
        red: (draw.find((item) => item.colour === "red") ?? 0).num ?? 0,
        blue: (draw.find((item) => item.colour === "blue") ?? 0).num ?? 0,
      };
    });
    return {
      "Game Num": gameNum,
      draws,
    };
  });

//part 1

const maxGreen = 13;
const maxRed = 12;
const maxBlue = 14;

const part1 = formattedInput
  .filter((game) =>
    game.draws.every(
      (draw) =>
        draw.green <= maxGreen && draw.red <= maxRed && draw.blue <= maxBlue
    )
  )
  .map((game) => parseInt(game["Game Num"]))
  .reduce((a, b) => a + b);

console.log(part1);

//part2

const part2 = formattedInput
  .map((game) => {
    const maxGreen = Math.max(...game.draws.map((draw) => draw.green));
    const maxRed = Math.max(...game.draws.map((draw) => draw.red));
    const maxBlue = Math.max(...game.draws.map((draw) => draw.blue));

    return maxGreen * maxRed * maxBlue;
  })
  .reduce((a, b) => a + b);

console.log(part2);
