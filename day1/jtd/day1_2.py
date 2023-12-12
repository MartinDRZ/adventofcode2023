import re
from number_parser import parse

def calibration_vals(line):
    regex_patterns = f'({")|(".join(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])})'
    extract_number_words = [parse(n) for n in re.split(regex_patterns, line) if n != None and n != "\n" and n != ""]
    extract_number_from_jumble = [x for n in extract_number_words for x in re.findall(r"[0-9]", n)]
    return int("".join([str(extract_number_from_jumble[0]), str(extract_number_from_jumble[-1])]))
    # If you really want a one-liner... disgusting... this function is barely readable as it is...
    # return int("".join([str([x for n in [parse(n) for n in re.split(f'({")|(".join(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])})', line) if n != None and n != "\n" and n != ""] for x in re.findall(r"[0-9]", n)][0]), str([x for n in [parse(n) for n in re.split(f'({")|(".join(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])})', line) if n != None and n != "\n" and n != ""] for x in re.findall(r"[0-9]", n)][-1])]))

with open("input", "r") as input:
    print(sum([calibration_vals(line) for line in input.readlines()]))