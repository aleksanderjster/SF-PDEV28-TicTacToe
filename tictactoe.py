## ==================================
##
## Output the game field with entered values.
## Request for user input. if step is odd then players "X" turn otherwise "0"
## Check if selected address is not occupied.
## Check if winning case occur.
## check if input step does not exceed 9 (end of game with 'No winner')
##

## ==================================
## global variable
## ==================================
# game field with empty values
game_field = [[f' ' for col in range(3)] for row in range(3)]



## ==================================
## Game field output
## ==================================
def field_print():
    r = 0 # row indicator

    # printing game field header
    print('\n')
    print(f'  | 0 | 1 | 2 |')
    print(f'---------------')
    
    for row in game_field:
        r += 1
        str = f'{r-1} |' 
        
        for cell in row:
            str += f' {cell} |' # composing row

        # printing row and rows separator  
        print(str)
        print(f'---------------')



## ==================================
## Input verification
## ==================================
def input_verification(usr_input):
    
    usr_inp = usr_input.split()
    
    if len(usr_inp) > 2: return # enterd more than 2 values
    
    if not (usr_inp[0].isnumeric() and usr_inp[1].isnumeric()): return #  value is not numeric

    usr_inp = list(map(int, usr_inp))
    if (0 <= usr_inp[0] < 3) and (0 <= usr_inp[1] < 3):
        return usr_inp



## ==================================
## Request value:
## ==================================
def get_user_input(sign='0'):

    print(f'It is plaer "{sign}" turn')
    usr_input = input('Enter row and column numbers separated with space\nrow col: ')
    return usr_input



## ==================================
## Vacancy check
## ==================================     
def fill_cell(cell, sign):
    if game_field[cell[0]][cell[1]] == ' ':
        game_field[cell[0]][cell[1]] = sign
        return True
    else:
        return False

    
## ==================================
## Get row values
## ==================================
def row_values(row):
    return game_field[row]



## ==================================
## Get column values
## ==================================
def column_values(column):
    return list(map(lambda x: x[column], game_field))



## ==================================
## Get column values
## ==================================
def diagonal_values(direction=True):
    col = 0
    dia = []
    for row in game_field:
        if direction:
            dia.append(row[col])
        else:
            dia.append(list(reversed(row))[col])
        col += 1
    return dia
        


## ==================================
## Winner check
## ==================================
def is_winner(sign):

    #check for rows
    for i in range(3):
        check = all(list(map(lambda x: x == sign, row_values(i))))
        if check: return True
    for i in range(3):
        check = all(list(map(lambda x: x == sign, column_values(i))))
        if check: return True
    check = all((list(map(lambda x: x == sign, diagonal_values()))))
    if check: return True
    check = all((list(map(lambda x: x == sign, diagonal_values()))))
    if check: return True

    return False




## ==================================
## main entrance into the game
## ==================================
def main():
    step = 0
    field_print()

    step += 1
    input_verified, cell_filled = False, False
    is_game_over = False
    
    while True:        

        # defines what players turn
        if step % 2 == 1:
            sign = 'X'
        else:
            sign = '0'
            
        usr_input = get_user_input(sign)

        # verifying input
        usr_input = input_verification(usr_input)        
        if usr_input:
            print('INFO: input verified')
            input_verified = True
        else:
            print('WARNING: input is not verified!\n')

        if input_verified:
            cell_filled = fill_cell(usr_input, sign)
            if cell_filled:
                step += 1 # initialization of next turn
                field_print()
                is_game_over = is_winner(sign)
                input_verified = False

            else:
                print('WARNING: Cell is not free for input.\n') 
            
        if step > 9:
            is_game_over = True
            print('\n' + '='*20)
            print('No winner this time!')
            break

        if is_game_over:
            print(f'\nCONGRATULATION: Player "{sign}" is winner.')
            break # end of game
        



if __name__ == '__main__':
    main()
