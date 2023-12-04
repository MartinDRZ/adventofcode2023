#Solution to Day 1?
import re;
file = 'input.txt';
runTotal = 0;

fileContents = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None);
lines = fileContents.readlines();
fileContents.close();

#day1 part 1

for x in lines:
    newX = re.findall(r'\d', x);
    runTotal += int(newX[0]+newX[-1], base=10);

print("day1 part1 =", runTotal);

#day1 part 2

