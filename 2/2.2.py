import re
file_path = './2/input.txt'

green = 'green'
red = 'red'
blue = 'blue'

def get_number(input):
    match = re.search(r'\d+', input)
    return int(match.group())
    

def calculate_valid(turns):
    colors_map = {}
    for i, turn in enumerate(turns):
        cubes = turn.strip().split(',')
        for cube in cubes:
            x = cube.strip().split(' ')
            color = x[1]
            number = get_number(cube)
            colors_map[color] = number if number > colors_map.get(color, 0) else colors_map.get(color, 0)
    return colors_map
        

with open(file_path, 'r') as file:
    lines = file.readlines()
    power = 0
    for line in lines:
        splitted_line = line.strip().split(':')
        game_number = get_number(splitted_line[0])
        turns = splitted_line[1].strip().split(';')
        valid = True
        colors_map = calculate_valid(turns)
        power = power + (colors_map[green] * colors_map[red] * colors_map[blue])
    print(power)
