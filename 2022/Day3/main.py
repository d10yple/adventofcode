# coded by d10yple
# Advent of code Day 3

def main() -> None:
    #alphabet (lower & upper)
    base_alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_score_first_puzzle, final_score_second_puzzle = 0, 0
    second_puzzle_three_line_set = []
    
    with open('inputs.txt', 'r') as file: # open input files
        
        for count, lines in enumerate(file, start=1): # looping through lines
            """
            First puzzle
            """
            line = lines.strip() # single line
            half = int((len(lines)-1)/2) # half ruckstack
            match_item = list(set(line[0:half]) & set(line[half:])) # match item between two compartments 
            final_score_first_puzzle+=base_alpha.index(match_item[0])+1 # defining score
            
            """
            Second puzzle
            """
            second_puzzle_three_line_set.append(line) # adding current line to the stack
            if count%3==0: # if stacksize is 3
                # find a match between those three lists
                match_puzzle_two = list(set(second_puzzle_three_line_set[0]) & set(second_puzzle_three_line_set[1]) & set(second_puzzle_three_line_set[2]))
                final_score_second_puzzle+=base_alpha.index(match_puzzle_two[0])+1 # adding to the score
                second_puzzle_three_line_set = [] #clearing the list to restart
                           
    print(final_score_first_puzzle) # puzzle 1 score
    print(final_score_second_puzzle) # puzzle 2 score
    
if __name__ == "__main__":
    main()