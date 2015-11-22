class Node:
    def __init__(self,data):
        self.data = data
        self.visited = 0
        self.next = None
        
#Constructing the linked list of the graph nodes
# ටීයුට් එකේ තියෙන graph එක හදන්න කම්මැලී.
# සර් DFS නෝට් එකේ දුන්න example graph එක හදමු.
# U,V,W,X,Y,Z එක.

v1_1 = Node(2)
v1_2 = Node(4)
v1_1.next = v1_2

v2_1 = Node(5)

v3_1 = Node(5)
v3_2 = Node(6)
v3_1.next = v3_2

v4_1 = Node(2)

v5_1 = Node(4)
v6_1 = None
#this is the graph
''' 
   2(V)==>4(X)
   5(Y)
   5(Y)==>6(Z)
   2(V)
   4(X)
   None
'''
aje_list = [v1_1,v2_1,v3_1,v4_1,v5_1,v6_1]

#just to be clear enough I'll assign letters to vertexes i.e. 1=>U, 2=>V ...
aje_list_values = ["U","V","W","X","Y","Z"]

color = []
predecessors = []
dicoverTimes = []
finalTimes = []
time = 0
def dfs(graph):
    for i in range(len(graph)):
        color.append("white")
        dicoverTimes.append(None)
        finalTimes.append(None)
        predecessors.append(None)
    global time
    time = 1
    for i in range(len(graph)):
        if(color[i]=="white"):
            dfsVisit(i)
def dfsVisit(u):
    color[u] = "gray"
    global time
    dicoverTimes[u] = time
    time = time+1
    node = aje_list[u]
    while(node != None):
        v = node.data-1
        if(color[v]=="white"):
            predecessors[v]=u
            dfsVisit(v)
        node = node.next
    color[u] = "black"
    print(aje_list_values[u])
    finalTimes[u] = time
    time = time+1
#Calling dfs function
dfs(aje_list)

#printing other related data
for i in range(len(aje_list)):
   print("-------------------------------")
   print("            "+aje_list_values[i])
   print("Discover time : "+str(dicoverTimes[i]))
   print("Final time    : "+str(finalTimes[i]))
   if(predecessors[i]!=None):
      print("Predecessor   : "+str(aje_list_values[predecessors[i]]))
   else:
      print("Predecessor   : "+str(predecessors[i]))
   print("-------------------------------")

    
