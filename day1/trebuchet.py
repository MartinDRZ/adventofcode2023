#Solution to Day 1?

import re

with open("/home/martin/git-clones/adventofcode2023/files/md_files/day1_input","r") as calnum:
    for line in calnum:
        nums = re.findall("[0-9]", line)
        lastnumindex = len(nums) - 1
        firstnum = nums[0]
        lastnum = nums[lastnumindex]
        final num = 