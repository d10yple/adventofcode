def main():
    size = 9 # amount of crates stacks the boat can handle
    puzzle_two = True # puzzle 1 or puzzle 2
    
    boatstacks = {} # list of all crates stack
    for _ in range(1, size+1):
        boatstacks[_] = []
    
    with open(file="inputs.txt", mode="r") as input_file:
        all_lines = []
        instructions = []
        
        # It's a bit complicated to fill lists from empty (text file) so we will 
        # perform a transformation in this first loop to, firstly separate 
        # the instructions from the crates and secondly process the first lines. 
        # If the position of a space is even then it is necessarily the edges of a crate
        # (the direction of the brackets is determined by the boolean), if this is not 
        # the case we will simply fill the void with points to be able to process the line 
        # in a better way a bit later.
        
        for line in [lines for lines in input_file]:
            if line[0] != 'm':
                l = ''
                v = True
                for i, c in enumerate(line):
                    if i % 2 == 0:
                        l+='[' if v else ']'
                        v = not v
                    else:
                        if line[i] == ' ':
                            l+="."
                        else: 
                            l+=c
                all_lines.append(l)
                
            #Regarding the instructions, we will only keep the 
            #numbers to optimize our loops
            else:
                instruction = []
                for instr in line.split():
                    if instr.isdigit():
                        instruction.append(int(instr))
                        
                instructions.append(instruction)
           
        # In this second loop, we will clean up the previous lines. 
        # Remember, we filled all the spaces with dots, inside the 
        # brackets included (value of the box). So here we will identify 
        # the location of these potential values and replace them with 
        # another character (different from the dot) for better visibility.
        
        formatted_lines = [] 
        
        for line in all_lines:
            l = ''
            for i, c in enumerate(line):
                if not i % 2 == 0 and not line[i].isalpha():
                    if line[i-1] == '[' and line[i+1] == ']':
                        l += '_'
                    else: 
                        l+=c
                else:
                    l+=c 
                    
            # here we're filling formatted_lines replacing _ by None 
            g = []
            for c in l:
                if c.isalpha():
                    g.append(c)
                elif c == "_":
                    g.append(None)
                    
            formatted_lines.append(g)
        
        # here we're filling the boat correctly (index of crate in the right index of the stack)
        for element in formatted_lines[::-1]:
            for i, crate in enumerate(element, start=1):
                if not crate == None:
                    boatstacks[i].append(crate)
                    
    #Once the boat is full we can proceed to carry out the crane's instructions.
    for instruction in instructions:
        move_amount, move_from, move_to = instruction[0], instruction[1], instruction[2]
        moved_parts = boatstacks[move_from][len(boatstacks[move_from])-move_amount:len(boatstacks[move_from])+move_amount]
        
        # two solutions (puzzle 1 and 2)
        if not puzzle_two:
            boatstacks[move_to].extend(moved_parts[::-1])
        
        else:
            boatstacks[move_to].extend(moved_parts)
            
        boatstacks[move_from] = boatstacks[move_from][:-move_amount]

    #filling final output string
    passcode = ''
    for key, value in boatstacks.items():
        passcode+=value[-1]
        
    print(passcode)
    
if __name__ == "__main__":
    main()