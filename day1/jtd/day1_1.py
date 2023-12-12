import re

def calibration_vals(line):
    return int("".join([re.findall(r"[0-9]", line)[0], re.findall(r"[0-9]", line)[-1]]))

with open("input", "r") as input:
    print(sum([calibration_vals(line) for line in input.readlines()]))