
cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    line[0] = float(line[0])
    line[1] = float(line[1])

    mass = line[0] * line[1]
    mass1 = str(round(mass, 2))

    print(mass1)
