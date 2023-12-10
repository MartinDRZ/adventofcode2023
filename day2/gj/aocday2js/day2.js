const fs = require('node:fs');

const formattedInput = fs.readFileSync("input.txt", "utf-8").split("\n").map(line => line.split(/:\s|;\s/)).map(line => {
    const gameNum = line.shift().slice(5)
    const draws = [...line.map(draws => draws.split(/, /).map(draw => {
        const num = parseInt(draw.split(" ")[0]);
        const colour = draw.split(" ")[1];
        return {
            num,
            colour
        }
    }))]
    return {
        "Game Num": gameNum,
        draws: draws.map(draw => {
            return {
                green: draw.find(item => item.colour === "green") === undefined ? 0 : draw.find(item => item.colour === "green").num,
                red: draw.find(item => item.colour === "red") === undefined ? 0 : draw.find(item => item.colour === "red").num,
                blue: draw.find(item => item.colour === "blue") === undefined ? 0 : draw.find(item => item.colour === "blue").num
            }
        })
        
    }
}).map(game => {
    const possible = game.draws.map(draw => {
        if draw
    })
});

console.log(formattedInput)