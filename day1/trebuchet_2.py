import regex as re

def text_to_number(num):
        match num:
                case "one":
                    out = 1
                case "two":
                    out = 2
                case "three":
                    out = 3
                case "four":
                    out = 4
                case "five":
                    out = 5
                case "six":
                    out = 6
                case "seven":
                    out = 7
                case "eight":
                    out = 8
                case "nine":
                    out = 9
        return out

total = 0

with open("/home/martin/git-clones/adventofcode2023/files/md_files/day1_input","r") as calnum:
    for line in calnum:
        nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line,overlapped=True)
        print(nums)
        lastnumindex = len(nums) - 1
        firstnum = nums[0]
        print(firstnum)
        if len(firstnum) != 1:
            firstnum = text_to_number(firstnum)
            print(firstnum)
        lastnum = nums[lastnumindex]
        if len(lastnum) != 1:
            lastnum = text_to_number(lastnum)
        finalnum = int(str(firstnum) + str(lastnum))
        print(finalnum)
        total = total + finalnum
        print(total)