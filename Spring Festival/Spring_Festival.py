import matplotlib.pyplot as plt
import random
for m in range(3,20):
    people = []
    get = []
    for i in range(0,10000):
        money = 10000
        for j in range(0,m):
            people.append(j+1)
            avg = money / (m-j) * 2
            if (j==(m-1)):
                nget = round(money,2)
            else:
                nget = random.uniform(0,avg)
                nget = round(nget,2)
            money = money - nget
            get.append(nget)

    plt.scatter(people,get)
    plt.show()