import re
file_path = './4/input.txt'    

def to_array_of_numbers(line):
    return re.findall(r'\d+', re.sub(r'^.*?:', '', line))

with open(file_path, 'r') as file:
    lines = file.readlines()
    mapped_lines = list(map(to_array_of_numbers, lines))
    cards = {index: 1 for index in range(len(mapped_lines))}
    for i, line in enumerate(mapped_lines):
        non_winning_numbers = set(line)
        nbr_of_winning_nbrs = len(line)-len(non_winning_numbers);
        for j in range(nbr_of_winning_nbrs):
            if(cards[i+j]):
                cards[i+j+1] = cards[i+j+1] + cards[i] 
        
    print(cards)    
    print(sum(cards.values()))
