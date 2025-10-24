PARTIES = None
CONSTIT = None
RESULTS = None

def menu():
    print("")
    print("1. Show constituencies")
    print("2. Show parties")
    print("3. Show results")
    print("9. Quit")
    print("")

    try:
        comand = int(input("Select an action: "))

        if comand in (1, 2, 3):
            return(comand)
        elif comand == 9:
            return(9)
        else:
            return(menu())

    except:
        return(menu())

#menu()

def constit():

    global CONSTIT

    #putting constituency in a dictionary
    if CONSTIT is None:

        d = {}

        file_name = input("File name: ")
        file_name = "/src/" + file_name

        try:

            with open (file_name, "r") as f:
                for line in f:
                    line = line.strip()

                    place, number = line.split(";")

                    d[place] = (number)

        except:
            return 0
        
        CONSTIT = d
            
    print("")
    print(f"{'Constituency':<20}{'Electorals':<10}")
    print("-" * 30)

    total = 0

    for k in CONSTIT:
        print(f"{k:<20}{CONSTIT[k]:>10}")

        number = int(CONSTIT[k])
        total += number

    total = str(total)
    print("-" * 30)
    print(f"{'Total:':<20}{total:>10}")

#constit()

def parties():

    global PARTIES

    #putting parties in a dictionary
    if PARTIES is None:

        d = {}

        file_name = input("File name: ")
        file_name = "/src/" + file_name

        try:

            with open (file_name, "r") as f:
                for line in f:
                    line = line.strip()

                    leter, name = line.split(";")

                    d[leter] = (name)

        except:
            return 0 
        
        PARTIES = d

    print("")
    print(f"{'List':<6}{'Party':>26}")
    print("-" * 32)

    for k in PARTIES:
        print(f"{k:<6}{PARTIES[k]:>26}")



#parties()

def results():

    global RESULTS
    global PARTIES
    global CONSTIT

    #putting results in a dictionary
    if RESULTS is None:

        d = {}

        file_name = input("File name for results: ")
        file_name = "/src/" + file_name

        try:

            with open (file_name, "r") as f:
                for line in f:
                    line = line.strip()

                    if ";" in line:
                        leter, votes = line.split(";")
                        d[place].append((leter, votes))
                        
                    else:
                        place = line
                        d[place] = []

        except:
            return 0 
        
        if PARTIES == None:
            return 0
        elif CONSTIT == None:
            return 0
        
        RESULTS = d

    place = input("Constituency: ")

    length = 0

    try:
        length = len(RESULTS[place])
    except:
            return 0 

    d = {}
    
    total = 0

    for i in range(length):
        votes = int(RESULTS[place][i][1])
        total += votes

    turnout = 100*(total/(int(CONSTIT[place])))
    turnout = round(turnout, 1)


    for i in range(length):
        d[i] = []

        leter = RESULTS[place][i][0]
        d[i].append(leter)

        name = PARTIES[leter]
        d[i].append(name)

        votes = int(RESULTS[place][i][1])
        d[i].append(votes)

        ratio = 100 * (votes/total)
        ratio = round(ratio, 1)
        d[i].append(ratio)





    print("")
    print(place) 
    print(f"{'List':<10}{'Party':>26}{'Votes':>10}{'Ratio':>10}")
    print("-" * 56)

    for i in range(length):
        print(f"{d[i][0]:<10}{d[i][1]:>26}{d[i][2]:>10}{d[i][3]:>10}")

    print("-" * 56)

    print(f"{'Total:':<36}{total:>10}{'100.0':>10}")
    print(f"{'Turnout:':<46}{turnout:>10}")


#results()

#runing the program

X = 0

while X != 9:

    X = menu()

    if X == 1:
        constit()
    elif X == 2:
        parties()
    elif X == 3:
        results()
