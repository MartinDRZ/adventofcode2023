const fs = require("fs");

//basic read and sort into sections

const input = fs
  .readFileSync("input.txt", "utf-8")
  .split(
    /seeds:\s|\n\nseed-to-soil\smap:\n|\n\nsoil-to-fertilizer\smap:\n|\n\nfertilizer-to-water\smap:\n|\n\nwater-to-light\smap:\n|\n\nlight-to-temperature\smap:\n|\n\ntemperature-to-humidity\smap:\n|\n\nhumidity-to-location\smap:\n/
  );

const formattedInput = {
  seeds: input[1].split(" "),
  "seed-to-soil map": input[2].
};

console.log(formattedInput);
