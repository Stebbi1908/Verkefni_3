def parties():

    print("List".ljust(19," "), "Party".rjust(10," ") )
    print("-" * 30)

    with open ("parties.txt", "r") as f:
        for line in f:
            line = line.strip()
            place, number = line.split(";")
            print(place.ljust(4," "), number.rjust(25," "))


parties()
