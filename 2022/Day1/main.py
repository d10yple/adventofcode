# Coded by d10yple
# adventofcode day 1

def main():
    calories = []; #list of all calories
    individual_calories = [] #list of individual calorie (to fill calories list)

    with open("inputs.txt", "r") as file: #opening file
        for lines in file: #throug each line of the file
            #append block of calorie to individual_calories to append to calories
            individual_calories.append(int(lines.strip())) if lines.strip() != "" else calories.append(individual_calories);
            #empty the cal to restart the loop and add another block
            individual_calories = [] if lines.strip() == "" else individual_calories
            
    total_calories = [sum(total) for total in calories] #total of calories on each individual
    total = sum([n for n in sorted(total_calories)[::-1][0:3]]) #sum of the top 3 individual
        
    #print data
    print(f"Max: {sorted(total_calories)[-1]}") # puzzle 1
    print(f"Sum of the 3 largest individuals: {total}") #puzzle 2

if __name__ == "__main__":
    main();