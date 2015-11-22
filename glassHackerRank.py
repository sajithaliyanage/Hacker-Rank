user = int(raw_input())
lists = []
final = []
dnum =[]
for i in range(user):
    lists.append(int(raw_input()))

lists.sort();
#print lists;

for i in range(len(lists)):
    if i ==0:
        final.append(lists[i])
    elif(i%2==0):
        final.append(lists[i])
    else:
        final.insert(0,lists[i])
#print final

for i in range(len(final)-1):
    if(final[i]>final[i+1]):
        dnum.append(final[i]-final[i+1])
    else:
        dnum.append(final[i+1]-final[i])

if final[0]>final[len(final)-1]:
    dnum.append(final[0]-final[len(final)-1])
else:
    dnum.append(final[len(final)-1]-final[0])
#print dnum
print max(dnum);

