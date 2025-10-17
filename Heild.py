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

def constit():
    print("Constituency".ljust(19," "), "Electorals".rjust(10," ") )
    print("-" * 30)

    heild = 0

    with open ("constit.txt", "r") as f:
        for line in f:
            line = line.strip()
            place, number = line.split(";")
            print(place.ljust(24," "), number.rjust(5," "))

            heild += int(number)

    heild = str(heild)
    print("-" * 30)
    print("")
    print("Total:".ljust(19," "), heild.rjust(10," ") )

#constit()

def parties():

    print("List".ljust(19," "), "Party".rjust(10," ") )
    print("-" * 30)

    with open ("parties.txt", "r") as f:
        for line in f:
            line = line.strip()
            place, number = line.split(";")
            print(place.ljust(4," "), number.rjust(25," "))


#parties()
