import regex as re
re_pattern = "[0-9]+"


with open("/home/martin/git-clones/adventofcode2023/files/md_files/day3_input.txt","r") as file:
    input_lines = file.readlines()
    line_count = len(input_lines)
    valid_part_numbers = []
    for count, input_line in enumerate(input_lines):
        print("line is of length " + str(len(input_line)))
        line_numbers = re.finditer(re_pattern, input_line)
        for match in line_numbers:
            if int(match.start()) - 1 < 0:
                before = 0
            else:
                before = int(match.start()) - 1
            after = int(match.end()) + 1
            found_chars_sameline = input_line[before:after]
            linebeforecount = count - 1
            if linebeforecount < 0:
                linebefore = ""
            else:
                linebefore = input_lines[linebeforecount]
            found_chars_linebefore = linebefore[before:after]
            lineaftercount = count + 1
            if lineaftercount >= line_count:
                lineafter = ""
            else:
                lineafter = input_lines[lineaftercount]
            found_chars_lineafter = lineafter[before:after]
            string_test = found_chars_lineafter + found_chars_linebefore + found_chars_sameline
            for char in string_test:
                match_char = re.search("(\.|[0-9])", char)
                if not match_char:
                    print(char + " is not a number or a . - adding " + str(match.captures()) + " to valid part numbers list")
                    valid_part_numbers.append(int(match.captures()[0]))
                    break
                else:
                    print(match_char.captures())
    print(sum(valid_part_numbers))