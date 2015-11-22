gap = [];
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;
    def __str__(self):
        return str(self.data);
def bfs(graph,source):
    final = "";
    Queue = [];
    color = []
    distance = []
    count = []
    for i in range(len(graph)):
        color.append("White");
        distance.append(None);
        count.append(None);

    color[source-1] = "Gray";
    distance[source-1] = 0;
    count[source-1] = 0;
    Queue.append(source)

    while(len(Queue)!=0):
        u = Queue.pop(0);
        #print u;
        node = graph[u-1]
        while(node!=None):
            if(color[node.data-1] =="White"):
                Queue.append(node.data);
                color[node.data-1] ="gray"
                distance[node.data-1] = distance[u-1] + 1;
            count[node.data-1] = count[u-1]+ gap[u-1];
            node = node.next;
            print count;
        color[u-1] = "black"
    


    for i in range(len(graph)):
        if(i==start-1):
            pass
        else:          
            if(count[i]==None):
                final += "-1 ";
            else:
                final += str(count[i])+" ";
                    
    return final.strip();

cases = int(raw_input());

while(cases>0):
        
    inputs = raw_input();
    num  = map(int,inputs.split(" "));
    vertex = int(num[0]);
    edges = int(num[1]);
    

    graph = [];
    for i in range(vertex):
        graph.append(None);

    for i in range(edges):
        edge = map(int,raw_input().split(" "));
        fromVertex  = int(edge[0]);
        toVertex = int(edge[1]);
        differentWeight = int(edge[2]);
        gap.append(differentWeight);
        node = Node(toVertex);
        
        if(graph[fromVertex-1]==None):
            graph[fromVertex-1] = node;
        else:
            node.next = graph[fromVertex-1];
            graph[fromVertex-1] = node;

        node = Node(fromVertex);
        
        if(graph[toVertex-1]==None):
            graph[toVertex-1] = node;
        else:
            node.next = graph[toVertex-1];
            graph[toVertex-1] = node;

    start = int(raw_input());
    print bfs(graph,start)
    cases -= 1; 

    '''
    def isPath(n1,n2):
        p = False;
        n = graph[n1-1];
        
        while(n!=None):
            if (n.data == n2):
                print ("There is an edge");
                p = True;
                break;
            n = n.next;

        if(p==False):
            print("There is no edge");
        
    isPath(fromVertex,toVertex)
    '''

     
       
       
   




























