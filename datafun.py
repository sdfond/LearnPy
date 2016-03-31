import csv
import numpy as np

def smooth(lst):
    ret = []

    ret.append((lst[-1]+sum(lst[0:2]))/3)
    for i in range(1,len(lst)):
        ret.append(sum(lst[i-1:i+1])/3)
    ret.append((lst[0]+sum(lst[-2:]))/3)
    return ret


f = open('test.csv')
csv_f = csv.reader(f)

lst = []
cnt = 1
for row in csv_f:
    if int(row[0]) == cnt:
        lst.append(float(row[2]))
#        print row[2]
    else:
        ret = smooth(lst)
        pos = sum(x > 0 for x in ret)
        neg = sum(x < 0 for x in ret)
        if pos > neg:
            print cnt,1
        elif pos < neg:
            print cnt,-1
        else:
            print cnt,0
        lst = []
        cnt += 1
#        if cnt > 3:
#            break
ret = smooth(lst)
pos = sum(x > 0 for x in ret)
neg = sum(x < 0 for x in ret)
if pos > neg:
    print cnt,1
elif pos < neg:
    print cnt,-1
else:
    print cnt,0
        
