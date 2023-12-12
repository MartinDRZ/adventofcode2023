import regex as re

def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    return max(int(count) for count, color in cubes if color == comparison_color)

with open("/home/martin/git-clones/adventofcode2023/files/md_files/day2_input","r") as games:
    input_lines = games.read().splitlines()
    set_multiples = []
    for line in input_lines:
        set_multiples.append(max_cubes(line, 'red') * max_cubes(line, 'green') * max_cubes(line, 'blue'))

print(sum(set_multiples))