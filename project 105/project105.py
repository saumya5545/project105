import csv
import math

with open('rawdata.csv',newline='')as f:
    reader=csv.reader(f)
    csvFiledata=list(reader)

randomnumber=csvFiledata[0]

def mean(data):
    n=len(data)
    total=0

    for i in data:
        total+=int(i)
    
    mean=total/n
    return mean

squared_list= []
for number in randomnumber:
    a = int(number) - mean(randomnumber)
    a= a**2
    squared_list.append(a)

sum=0

for i in squared_list:
    sum+=i

answer=sum/(len(randomnumber)-1)

standardDeviation=math.sqrt(answer)

print(standardDeviation)

