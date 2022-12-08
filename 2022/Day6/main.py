# coded by d10yple
# advent of code 2022 Day 6

def main() -> None:
    marker_found = False
    marker = 0
    puzzle_one = True
    startof_lenght = 4 if puzzle_one else 14
    
    # here we're formatting the datastream buffer into a list
    with open(file='inputs.txt', mode='r') as input_file:
        for lines in input_file:
            datastream_buffer = [line for line in lines][:-1]
        
    # while whole list is checked and there is no marker found
    while marker < len(datastream_buffer) and not marker_found:
        if marker > 2: # to avoid index out of range
            potential_starf_of_packet_marker = []
            k = 0
            while k < startof_lenght: # puzzle 1 and 2 depending bool of puzzle_one
                potential_starf_of_packet_marker.append(datastream_buffer[marker-k])
                k+=1
                
            # using set to compare, if set length is the same than list (potential)
            # length then, the last 3 characters behind marker are different 
            # and it's the starting point of the start-of-packet/message
            if len(set(potential_starf_of_packet_marker)) == len(potential_starf_of_packet_marker):
                print(f'marker is : {marker+1}')
                marker_found = True
                
        marker+=1

if __name__ == "__main__":
    main()