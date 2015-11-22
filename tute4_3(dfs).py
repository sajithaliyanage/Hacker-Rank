class Node:
   def __init__(self,data):
      self.data = data
      self.visited = 0
      self.next = None
class Stack:
   def __init__(self):
      self.stack = []
   def push(self,data):
      self.stack.append(data)
   def pop(self):
      return self.stack.pop()
   def isEmpty(self):
      return len(self.stack)==0

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

colors = []
time = 0 #time count
dTime = [] #discover times
fTime = [] #final times
predecessor = []

def dfs(graph):
   stack = Stack()
   global time
   for i in range(len(graph)):
      colors.append("White")
      dTime.append(None)
      fTime.append(None)
      predecessor.append(None)
   for i in range(len(graph)):
      if(colors[i]=="White"):
         colors[i] = "Gray"
         time = time+1
         dTime[i] = time
         pred = i
         stack.push(i)
         node = aje_list[i]
         while(node!=None):
            v = node.data-1
            if(colors[v]=="White"):
               colors[v] = "Gray"
               time = time+1
               dTime[v] = time
               predecessor[v]=pred
               pred = v
               stack.push(v)
               node = aje_list[v]
            else:
               #getting a adjecent node to v which is white
               while(node!=None and colors[node.data-1]!="White"):
                  node = node.next
      while(not stack.isEmpty()):
         time = time+1
         vertex = stack.pop()
         colors[vertex] = "Black"
         fTime[vertex] = time
         print(aje_list_values[vertex])
#calling dfs         
dfs(aje_list)

#printing other related data
for i in range(len(aje_list)):
   print("-------------------------------")
   print("            "+aje_list_values[i])
   print("Discover time : "+str(dTime[i]))
   print("Final time    : "+str(fTime[i]))
   if(predecessor[i]!=None):
      print("Predecessor   : "+str(aje_list_values[predecessor[i]]))
   else:
      print("Predecessor   : "+str(predecessor[i]))
   print("-------------------------------")
