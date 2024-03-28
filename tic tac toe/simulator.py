from definitions import state
from copy import copy, deepcopy
import sys

# A function which takes a state as input, and simulates a specific next move, specified by the possibility number
def make_move(state_variable,possibility_number):
    identified_possibility_number = 0
    simulated_state = state()
    simulated_state = simulated_state.copy_state(state_variable)
    identified_row = 0

    # Find grid position for the specified possibility number
    for row in simulated_state.grid:
        identified_column = 0
        for entry in row:
            if (entry == "_"):
                identified_possibility_number += 1
                
                # If the specified possibility number is reached, simulate move
                if (identified_possibility_number == possibility_number):
                    simulated_state.grid[identified_row][identified_column] = simulated_state.turn
                    if (simulated_state.turn == "X"):
                        simulated_state.turn = "O"
                    elif (simulated_state.turn == "O"):
                        simulated_state.turn = "X"
                    simulated_state.round_number += 1
                    simulated_state.current_status = simulated_state.check_status()
                
            identified_column += 1
        identified_row +=1
    
    return simulated_state


# A function which takes a state as input, simulates all possible immediate turns, and returns the list of possible next states
def simulate_one_round(state_variable):
    round_number = state_variable.round_number
    possible_states = []

    # If another round is to be played
    if(state_variable.check_status() == "draw"):
        # Iterate through remaining empty positions
        for possibility_number in range(1,(10-round_number)):
            possible_move = make_move(state_variable,possibility_number)
            possible_states.append(possible_move)

    return possible_states

# A function which finds the expected result of a given state
def simulate_result(state_variable):
    simulated_state = state()
    simulated_state = simulated_state.copy_state(state_variable)    

    simulated_state.current_status = simulated_state.check_status()

    if (simulated_state.current_status != "draw" or simulated_state.round_number == 9):
        simulated_state.expected_result = simulated_state.current_status
    else:
        possible_states = simulate_one_round(simulated_state)
        expected_result_found = False
        simulated_state.expected_result = "draw"
        if simulated_state.turn == "X":
            simulated_state.expected_result = "O wins"
        elif simulated_state.turn == "O":
            simulated_state.expected_result = "X wins"

        for possible_state in possible_states:
            if expected_result_found == False:
                result = simulate_result(possible_state)
                if simulated_state.turn == "X":
                    if result == "X wins":
                        expected_result_found = True
                        simulated_state.expected_result = "X wins"
                    elif result == "draw":
                        simulated_state.expected_result = "draw"
                elif simulated_state.turn == "O":
                    if result == "O wins":
                        expected_result_found = True
                        simulated_state.expected_result = "O wins"
                    elif result == "draw":
                        simulated_state.expected_result = "draw"

    return simulated_state.expected_result

# Function to simulate the best game from both sides, given a starting point
def simulate_best_game(state_variable):
    simulated_state = state()
    simulated_state = simulated_state.copy_state(state_variable)

    simulated_state.current_status = simulated_state.check_status()

    if (simulated_state.current_status != "draw" or simulated_state.round_number == 9):
        return
    else:
        result_to_play = simulate_result(simulated_state)
        possible_states = simulate_one_round(simulated_state)
        expected_result_found = False
        for possible_state in possible_states:
            if expected_result_found == False:
                result = simulate_result(possible_state)
                if result == result_to_play:
                    possible_state.print_grid()
                    simulate_best_game(possible_state)
                    expected_result_found = True
                    return

# Create the initial state object to be used for simulation
state0 = state()
state0.grid = [["X","O","_"],
                ["_","_","_"],
                ["_","_","_"]]
state0.turn = "X"
state0.round_number = 2
state0.print_grid()
counter = 0
print(simulate_result(state0))
simulate_best_game(state0)