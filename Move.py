# Move

# -------- part 1 -------- 

print ("Position in [1..10]:")

position = int(input())

# makes sure that the input is a number

while (1 > position) or (position > 10):

        print ("Position in [1..10]:")
        position = int(input())

before = position - 1

after = 10 - position

for i in range (0, before):
        print("x", end="")

print ("o", end="")

for j in range (0, after):
        print("x", end="")
        
print("")
print("l: left")
print("r: right")
print("Move:")

# -------- part 2 -------- 

# Skoða hvort inntak sé l, r eða annað
        
while True:
    move = input()

    if move == "l":
        if position > 1:
            position = position - 1
    elif move == "r":
        if position < 10:
            position = position + 1
    else:
          break

    before = position - 1

    after = 10 - position

    for i in range (0, before):
            print("x", end="")

    print ("o", end="")

    for j in range (0, after):
            print("x", end="")
        
    print("")
    print("l: left")
    print("r: right")
    print("Move:")
