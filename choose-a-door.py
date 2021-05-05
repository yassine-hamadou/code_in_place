def main():
    print("Welcome to the codeInPlace Game show")
    print("Pick a door and win a prize")
    print("------------------------------------")

    #Part 1: get door number from user
    while True:
        door = int(input("Door: "))
        #If no door is given input, keep prompting
        if not door:
            print("Please, you have to choose a door! ") 
            continue

        #Else if the input is invalid
        elif door < 1 or door > 3:
            #tell user the input was invalid
            print("Invalid door!")
        else:
            break
  
    #Part 2: compute the prize
    prize = 4
    if door == 1:
        prize =  2 + 9 // 10 * 100  #prize = 2 instead
    elif door == 2:
        locked = prize % 2 != 0
        if not locked:
            prize += 6  #prize = 10 instead
    elif door == 3:
        for i in range(door):
            prize += i  #prize = 7 instead

    #Part 3: report prize
    print(f"You win {prize} treats")

if __name__ == '__main__':
    main()



