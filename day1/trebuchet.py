#Solution to Day 1?
import regex as re;
file = 'input.txt';
total1 = 0;

fileContents = open(file, 'r');
lines = fileContents.readlines();
fileContents.close();

#day1 part 1

for x in lines:
    newX = re.findall('\d', x);
    total1 += int(newX[0]+newX[-1]);

print("day1 part1 =", total1);

#day1 part 2

total2 = 0

dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def strToNum(item):
    if item in dict.keys():
        return dict[item];
    else:
        return item;

for x in lines:
    newX = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', x, overlapped=True)
    numsX = map(strToNum, newX);
    listNumsX = list(numsX);
    total2 += int(listNumsX[0]+listNumsX[-1]);

print('day1 part2 =', total2);