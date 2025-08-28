dicttemp = {1:2,2:3}
for i, j in dicttemp.items():
    dicttemp[i] = 0
    del dicttemp[i]
print(dicttemp)