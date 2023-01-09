
for n in range(5):
    print('in outer loop', n)
    if(n==3):
        break
    for j in range(3):
        if(j==2 and n==2):
            print("reached condition")
            break
        else:
            print(n,'-', j)