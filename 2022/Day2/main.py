# Coded by d10yple
# adventofcode day 2

class RockPaperScissors:    
    """
    Class of the Day 2 Advent of code puzzle
    
    """
    def __init__(self, input_path : str) -> None:
        """
        Constructs all the necessary attributes for the RockPaperScissors object.

        Parameters
        ----------
            input_path : str
                path to the input data of the puzzle
        """
        self.input_path = input_path
        
    @property
    def final_user_score_first_puzzle(self) -> int:
        """
        Return the final user score of the first puzzle

        """
        score = 0
        for strategy_line in self.strategy_sheet:
            score+=self.first_puzzle(strategy_line[0], strategy_line[1])
            
        return score
    
    @property
    def final_user_score_second_puzzle(self) -> int:
        """
        Return the final user score of the second puzzle

        """
        score = 0
        for strategy_line in self.strategy_sheet:
            score+=self.second_puzzle(strategy_line[0], strategy_line[1])
            
        return score
        
    @property
    def strategy_sheet(self) -> list:
        """
        Return a list containing list of symbols used in
        the game 
        
        ex: [["A", "X"], ["B", "Y"], ...]

        """
        strategy_list = []
        with open(self.input_path, 'r') as file:
            for file_lines in file:
                strategy_list.append([file_lines.strip()[0], file_lines.strip()[2]])
                
        return strategy_list;
    
    @staticmethod
    def first_puzzle(first_letter : str, second_letter : str) -> int:
        """
        Return the score of a single battle between 
        two symbol in the first puzzle
        
        ex: ["A", "X"] : score = 4 (rock-rock)

        """
        return {
            "A": {             # it's a rock
                "X": 3+1,      # rock - rock(+1)(+3 cause draw)
                "Y": 6+2,      # rock - paper(+2)(+6 cause win)
                "Z": 0+3       # rock - scissors(+3)(+0 cause lose)
            }[second_letter], 
            "B": {             # it's paper
                "X": 0+1,      # paper - rock(+1) (+0 cause lose)
                "Y": 3+2,      # paper - paper(+2)(+3 cause draw)
                "Z": 6+3       # paper - scissors(+3)(+6 cause win)
            }[second_letter],
            "C": {             # it's scissors
                "X": 6+1,      # scissors-rock(+1)(+6 cause win)
                "Y": 0+2,      # scissors-paper(+2)(+0 cause lose)
                "Z": 3+3       # scissors-scissors(+3) (+3 cause draw)
            }[second_letter],
        }[first_letter]
    
    @staticmethod
    def second_puzzle(first_letter : str, second_letter : str) -> int:
        """
        Return the score of a single battle between 
        two symbol in the second puzzle
        
        ex: ["A", "X"] : score = 3 (need to loose on rock)

        """
        return {
            "X": {             # need loose (+0 cause it's a lose)
                "A": 3+0,      # need loose on rock (+3 cause scissors)
                "B": 1+0,      # need loose on paper (+1 cause rock)
                "C": 2+0       # need loose on scissors(+2 cause paper)
            }[first_letter], 
            "Y": {             # need draw (+3 cause it's a draw)
                "A": 1+3,      # need draw on rock(+1 cause rock)
                "B": 2+3,      # need draw on paper(+2 cause paper)
                "C": 3+3       # need draw on scissors(+3 cause scissors)
            }[first_letter],
            "Z": {             # need win (+6 cause it's a win)
                "A": 2+6,      # need win on rock(+2 cause paper)
                "B": 3+6,      # need win on paper(+3 cause scissors)
                "C": 1+6       # need win on scissors(+1 cause rock)
            }[first_letter],
        }[second_letter]
 
if __name__ == "__main__":
    rpc = RockPaperScissors('inputs.txt')
    print(rpc.final_user_score_first_puzzle)
    print(rpc.final_user_score_second_puzzle)