#It will ask until it gets 1 or 2 or 3 or 9
def menu():
    print("1. Show constituencies")
    print("2. Show parties")
    print("3. Show results")
    print("9. Quit")
    print("")

    try:
        comand = int(input("Select an action:"))

        if comand == (1 or 2 or 3):
            return(comand)
        elif comand == 9:
            return(0)
        else:
            return(menu())

    except:
        return(menu())

print(menu())
