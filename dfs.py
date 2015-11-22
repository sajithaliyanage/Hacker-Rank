class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;
    def __str__(self):
        return str(self.data);
    
def DFS(graph,root):
    visited = []
    stack = []
    stack.append(root);

    while(len(stack)>0):
        node = stack.pop();

        if node not in visited:
            visited.append(node)
            stack.extend([x for x in graph[node] if x not in visited])
    return visited;

        
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
        node = Node(toVertex);
 
        if(graph[fromVertex-1]==None):
            graph[fromVertex-1] = node;
        else:
            node.next = graph[fromVertex-1];
            graph[fromVertex-1] = node;

    start = int(raw_input());
    print DFS(graph,start)
    cases -= 1; 

       
   



























