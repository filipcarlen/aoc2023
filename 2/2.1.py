import re
file_path = './2/input.txt'
configuration = {'blue': 14, 'red': 12, 'green': 13}

def get_number(input):
    match = re.search(r'\d+', input)
    return int(match.group())
    

def valid_turn(turn):
    cubes = turn.strip().split(',')
    for cube in cubes:
        x = cube.strip().split(' ')
        color = x[1]
        number = get_number(cube)
        if number > configuration[color]:
            return False
    return True


with open(file_path, 'r') as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        splitted_line = line.strip().split(':')
        game_number = get_number(splitted_line[0])
        turns = splitted_line[1].strip().split(';')
        valid = True
        for turn in turns:
            if not valid_turn(turn):
                valid = False
        if valid:
            sum = sum + game_number
    print(sum)
