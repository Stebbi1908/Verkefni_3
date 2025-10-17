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

constit()
