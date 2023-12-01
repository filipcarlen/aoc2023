file_path = './1/input.txt'

textNumbers = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

def get_number(target_element):
    try:
        if target_element.isdigit():
            return target_element
        index = textNumbers.index(target_element)
        return str(index + 1)
    except ValueError:
        print(target_element)
        return None
    
def firstNumber(input_string):
    for i, _ in enumerate(input_string):
        candidate = input_string[0:i+1]
        for textNumber in textNumbers:
            if textNumber in candidate:
                return textNumber
            
def lastNumber(input_string):
     for i in range(len(input_string) - 1, -1, -1):
        candidate = input_string[i:len(input_string)]
        for textNumber in textNumbers:
            if textNumber in candidate:
                return textNumber

def find(input_string):
    first = firstNumber(input_string)
    last = lastNumber(input_string)
    return int(get_number(first) + get_number(last))

with open(file_path, 'r') as file:
    lines = file.readlines()
    sum = 0

    for line in lines:
        result = find(line)
        sum = sum + result
        
print(sum)


