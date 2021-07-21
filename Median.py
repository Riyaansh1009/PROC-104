import csv

with open('Data.csv', newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

newData = []
for i in range(len(data)):
    n = data[i][1]
    newData.append(float(n))

newData.sort()

lenght = len(newData)

if lenght%2==0:
    median1 = lenght/2
    median2 = (lenght/2) +1
    finalMedian = (median1 +median2)/2
else:
    finalMedian = newData[lenght/2]
print(finalMedian)





