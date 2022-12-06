# coded by d10yple
# Advent of code 2022 Day 4

def is_overlaping(assignement : list, strict_overlap : bool) -> bool:
    """Tell via bool if an assignement is overlaping (by its pair)

    Args:
        assignement (list): assignement
        strict_overlap (bool): feature of the second puzzle
                                only one section is required
                                to overlap

    Returns:
        bool: True if overlap, false if it's not
    """
    overlap = False # value tu return
    target_list = True # bool that will define on wich list we're working on
                       
    for _ in range(len(assignement)):
        current = {True: 0, False: 1}[target_list]    # define wich list
        
        for section in assignement[current]:          # for each section on the current assignement
            if section in assignement[not current]:   # if the section is present on the second assignement
                if strict_overlap:                    # stric overlap
                    # if max of current is less than the max from the other
                    # and the min of the current is more than the min of the current then..
                    if max(assignement[current]) <= max(assignement[not current]) and min(assignement[current]) >= min(assignement[not current]) :
                        overlap = True
                else: # not strict overlap
                    overlap = True
        
        target_list = not target_list
        
    return overlap

def main() -> None:
    """Main function
    """
    overlap_amount = 0      # amount of overlap (in the inputs)
    strict_overlap = False  # feature of the second puzzle
                            #  -> allow or not stric overlapping
    with open('inputs.txt') as file:  # open the file
        assignements = []             # empty assignement
        for lines in file:            # for lines in file
            i=0
            assignements_to_add = []  # assignement will be added in assignements list
            while i<2:
                # basically here, i'm formatting the input
                sections = lines.split(',')[i].replace('\n', '')
                a = [*range(int(sections.split('-')[0]), int(sections.split('-')[1])+1)]
                assignements_to_add.append(a)
                i+=1
                
            # formatted assignement added to the list
            assignements.append(assignements_to_add)
     
    # For each assignement, we add 1 in our overlap amount
    # if it's overlapping, 0 if not   
    for assignement in assignements:
        # reminder: stric_overlap is a feature of the second puzzle 
        overlap_amount+=1 if is_overlaping(assignement, strict_overlap) else 0

    # print out the result
    print(overlap_amount)

if __name__ == "__main__":
    main()