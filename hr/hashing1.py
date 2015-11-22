import random
randomInput = random.sample(range(1,1001),100)
table =[];

for i in range(100):
    table.append(None)

def h(val):
    return (((6*val+31)%103)%100)
    
def H(k,i):
    return ((h(k)+i)%100)

def addToTable(k):
    for i in range(100):
        pos = H(k,i)
        if(table[pos]==None):
            table[pos] = k;
            break;
            
for i in range(len(randomInput)):
    addToTable(randomInput[i]);

print table;
