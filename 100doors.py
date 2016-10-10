doors = []

def fill():
    for i in range(100):
        doors.append(0)

def show():
    print("The following doors are open:", end=" ")
    for i in range(100):
        if (doors[i]/2) != (int(doors[i]/2)):
            print(i+1, ",", end="")
    print("\b", " ")
    
fill()
for i in range(0,100):
    for j in range(i,100,i+1):
            doors[j] += 1           
show()