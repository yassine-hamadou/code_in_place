def main():
    stones_left = 20
    current_player = 1
    while stones_left > 0:
        print(f"There are {stones_left} stones left")
        stonesToRemove = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))
        if stonesToRemove == 1 or stonesToRemove == 2:
            inputIsInvalid = False
        else:
            inputIsInvalid = True
        while inputIsInvalid:
            stonesToRemove = int(input("Please enter 1 or 2: "))
            if stonesToRemove == 1 or stonesToRemove == 2:
                inputIsInvalid = False

        stones_left -= stonesToRemove
        current_player = change_turn(current_player)
        print("")

    print(f"Player {current_player} wins!")
        
        
def change_turn(current_player):
    if current_player == 1:
        return 2
    if current_player == 2:
        return 1 


if __name__ == '__main__':
    main()
