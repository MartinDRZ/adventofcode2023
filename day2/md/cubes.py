import regex as re

game_total = 0


def count_colours(colour_to_find, draw_colour):
    search = re.findall(colour_to_find, draw_colour)
    if len(search) != 0:
        if search[0] == colour_to_find:
            draw_num = re.findall('[0-9]+', draw_colour)
            draw_number = draw_num[0]
            return draw_number
    return 0

def iterate_game_count(game_num):
    global game_total
    game_total = game_total + int(game_num)
    return game_total
    

with open("/home/martin/git-clones/adventofcode2023/files/md_files/day2_test_input","r") as games:
    for line in games:
        colonsplit = line.split(':')
        #print(colonsplit)
        game_number_text = colonsplit[0]
        #print(game_number_text)
        game_num_list = re.findall('[0-9]+', game_number_text)
        game_num = game_num_list[0]
        game_text = colonsplit[1]
        draw_list = game_text.split(';')
        #print(draw_list)
        draw_iter = 0
        for draw in draw_list:
            child_break = False
            colours = draw.split(',')
            for colour in colours:
                red = 0
                red_test = False
                red = count_colours("red", colour)
                print(red)
                if int(red) <= 12:
                     red_test = True
                     print (str(red) + " is less than 12")
                     print(red_test)
                green = 0
                green_test = False
                green = count_colours("green", colour)
                if int(green) <= 13:
                     green_test = True
                     print (str(green) + " is less than 13")
                     print(green_test)
                blue = 0
                blue_test = False
                blue = count_colours("blue", colour)
                if int(blue) <= 14:
                     blue_test = True
                     print (str(blue) + " is less than 14")
                     print(blue_test)
                if red_test == True and blue_test == True and green_test == True:
                    tot = iterate_game_count(game_num)
                    draw_iter = draw_iter + 1
                    print("This is game number: " + str(game_num))
                    child_break = True
                    break
            if child_break == True:
                break
        print(game_total)