import random
먹이들 = []

for i in range(5):
    x , y = random.randint(0, 20),random.randint(0, 20)
    먹이들.append([x , y])

print(먹이들)

print("-------------------------")
for pos in 먹이들:
    print(pos,pos[0],pos[1])