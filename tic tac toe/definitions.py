from copy import copy, deepcopy

# A class which can hold the state of the game at any point of time
class state: 
    
    # A grid which shows the spots which are covered by Xs, Os or are empty
    grid = [["_","_","_"],["_","_","_"],["_","_","_"]]

    # Variable to indicate whose turn it is, X or O and which round number
    round_number = 0
    turn = "X"

    # Game status showing whether the game has been won by X, O or drawn
    # This will also show what the inevitable outcome is, assuming both players are playing their best possible game
    current_status = "draw"
    expected_result = "unknown"

    # Instantiation function
    def __init__(self):
        self.grid = [["_","_","_"],["_","_","_"],["_","_","_"]]
        self.round_number = 0
        self.turn = "X"
        self.current_status = "draw"
        self.expected_result = "unknown"

    # Function to assess the current status of the game
    def check_status(self):
        grid = self.grid
        status = "draw"
        # Check for row based wins
        for row in grid:
            if row == ["X","X","X"]:
                status = "X wins"
            if row == ["O","O","O"]:
                status = "O wins"
        
        # Check for column based wins
        for col in [0,1,2]:
            if (grid[0][col] == "X" and grid[1][col] == "X" and grid[2][col] == "X"):
                status = "X wins"
            if (grid[0][col] == "O" and grid[1][col] == "O" and grid[2][col] == "O"):
                status = "O wins"

        # Check for diagonal based wins
        if (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X"):
            status = "X wins"
        if (grid[2][0] == "X" and grid[1][1] == "X" and grid[0][2] == "X"):
            status = "X wins"
        if (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O"):
            status = "O wins"
        if (grid[2][0] == "O" and grid[1][1] == "O" and grid[0][2] == "O"):
            status = "O wins"
        
        # Update the status
        self.status = status
        return self.status
    
    # Function to print the grid and its contents
    def print_grid(self):
        grid = self.grid
        row_count = 1
        # Print each row of the grid
        for row in grid:
            entry_count = 1
            print("", end = " ")
            # Print each entry in the row
            for entry in row:
                if entry == "_":
                    print(" ", end = " ")
                else:
                    print(entry, end = " ")
                if(entry_count < 3):
                    print("|", end = " ")
                    entry_count += 1
                else:
                    print(" ")
            if (row_count < 3):
                print("---|---|---")
                row_count += 1
        
    # Function to copy the state of another state objoect
    def copy_state(self, state_to_copy):
        if state_to_copy.turn == "X":
            self.turn = "X"
        else:
            self.turn = "O"
        
        self.round_number = 0
        while self.round_number < state_to_copy.round_number:
            self.round_number += 1
        
        if state_to_copy.current_status == "X wins":
            self.current_status = "X wins"
        elif state_to_copy.current_status == "O wins":
            self.current_status = "O wins"
        else:
            self.current_status = "draw"

        if state_to_copy.expected_result == "X wins":
            self.expected_result = "X wins"
        elif state_to_copy.expected_result == "O wins":
            self.expected_result = "O wins"
        elif state_to_copy.expected_result == "draw":
            self.expected_result = "draw"
        else:
            self.expected_result = "unknown"

        row_number = 0
        for row in state_to_copy.grid:
            column_number = 0
            for entry in row:
                if entry == "X":
                    self.grid[row_number][column_number] = "X"
                elif entry == "O":
                    self.grid[row_number][column_number] = "O"
                else:
                    self.grid[row_number][column_number] = "_"
                
                column_number += 1
            row_number += 1

        return self