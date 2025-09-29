print ("Position in [1..10]:")

position = int(input())

#makes sure that the input is a number


while (1 > position) or (position > 10):

        print ("Position in [1..10]:")
        position = int(input())

print(position)

befoure = position - 1

after = 10 - position

for i in range (0,befoure):
        print("x", end="")

print ("o", end="")

for j in range (0, after):
        print("x", end="")
        
print("")
print("l: left")
print("r: right")
print("Move:")
