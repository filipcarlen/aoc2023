def find_first_digit(input_string):
    for char in input_string:
        if char.isdigit():
            return int(char)

    return None
    
def find_last_digit(input_string):
    for char in reversed(input_string):
        if char.isdigit():
            return int(char)
    
    return None

file_path = './1/input.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    sum = 0

    for line in lines:
        firstNumber = find_first_digit(line);
        lastNumber = find_last_digit(line);
        result = int(str(firstNumber) + str(lastNumber))
        sum = sum + result


print(sum)