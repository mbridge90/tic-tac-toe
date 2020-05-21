cells = list("_________")
move_count = 1

def print_board():
    print("""
    ---------
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    ---------
    """.format(cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7], cells[8]))



def insert_coordinates():
    coordinates = list(input("Enter the coordinates: "))
    if " " in coordinates:
        coordinates.remove(" ")
    try:
        coords_as_int = [int(coordinate) for coordinate in coordinates]
        if coords_as_int[0] in [1, 2, 3] and coords_as_int[1] in [1, 2, 3]:
            input_index = 8 - (3 * coords_as_int[1]) + coords_as_int[0]
            if cells[input_index] == "_":
                global move_count
                if move_count % 2:
                    cells[input_index] = 'X'
                    move_count += 1
                    print_board()
                    check_board()
                else:
                    cells[input_index] = 'O'
                    move_count += 1
                    print_board()
                    check_board()
            else:
                print("This cell is occupied! Choose another one!")
                insert_coordinates()
        elif coords_as_int[0] > 3 or coords_as_int[1] > 3:
            print("Coordinates should be from 1 to 3!")
            insert_coordinates()
    except ValueError:
        print("You should enter numbers!")
        insert_coordinates()
    except IndexError:
        print("Please enter two coordinates.")
        insert_coordinates()

def check_board():
    rows = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
    columns = [[cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]]]
    diagonals = [[cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]
    all_possible_wins = rows + columns + diagonals
    X_win = any([combo == ['X', 'X', 'X'] for combo in all_possible_wins])
    O_win = any([combo == ['O', 'O', 'O'] for combo in all_possible_wins])

    if X_win and not O_win:
        print("X wins")

    elif O_win and not X_win:
        print("O wins")

    elif not X_win and not O_win and '_' in cells:
        insert_coordinates()

    elif not X_win and not O_win and '_' not in cells:
        print("Draw")



def play_game():
    print_board()
    insert_coordinates()

play_game()




