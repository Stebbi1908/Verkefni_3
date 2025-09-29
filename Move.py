# Move

# Intent of code

# This program displays a 1 dimentional board of length in x-axis from 1 to 10 with a marker 'o'.
# The user chooses a valid starting position (1..10), then enters moves:
#   "l" to move left (unless at the left edge), "r" to move right (unless at the right edge)
#   any other input for example "q" to quit.
# After each move, the board is reprinted showing the updated position.


# -------- part 1 -------- 

print ("Position in [1..10]:")

position = int(input())

# makes sure that the input is a number

while (1 > position) or (position > 10):

        print ("Position in [1..10]:")
        position = int(input())

# Compute how many 'x' are before/after the marker for the initial render
before = position - 1

after = 10 - position

# Initial board render
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

# Process commands until a non l or r input is received for example "q"
        
while True:
    move = input()

    if move == "l":
        # Guard against moving beyond the left edge
        if position > 1:
            position = position - 1
    elif move == "r":
        # Guard against moving beyond the right edge
        if position < 10:
            position = position + 1
    else: 
          # Any other input ends the loop, for example "q"
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
