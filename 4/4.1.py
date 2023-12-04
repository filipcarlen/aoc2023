import re

file_path = './4/input.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    sum = 0;
    for line in lines:
        numbers = re.findall(r'\d+', re.sub(r'^.*?:', '', line))
        non_winning_numbers = set(numbers)
        nbr_of_winning_nbrs = len(numbers)-len(non_winning_numbers);
        if(nbr_of_winning_nbrs > 0):
            sum = sum + pow(2, nbr_of_winning_nbrs-1)
        
    print(sum)


