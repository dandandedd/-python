trigal = []
for j in range(11):
    trigal.append([])
    for k in range(j+1):
        trigal[j].append([]) #创立二维矩阵

for j in range (11):
    for k in range(j+1): 
        if k == 0 or j == k :
            trigal[j][k] = 1
        else :
            trigal[j][k] = trigal[j-1][k-1] + trigal[j-1][k] #给二维矩阵赋值

for j in range (11):
    for i in range(int(((11-j)//2))):
        print("\t",end = '')
    for k in range (j+1):
        if j % 2 == 0:
            print("    ",end = '')
        print(trigal[j][k],end = '\t')       
    print()