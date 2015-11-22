aMatrix = [];
'''
aMatrix.append([0,1,1,0,0]);
aMatrix.append([0,0,1,0,0]);
aMatrix.append([0,0,0,0,1]);
aMatrix.append([1,0,0,0,1]);
aMatrix.append([0,0,0,0,0]);
'''


def bfs(graph,s):
    indexVertex = s-1;
    Queue = [];
    color = []
    distance = []
    count = []
    for i in range(len(graph)):
        color.append("White");
        distance.append(None);
        count.append(None);

    color[indexVertex] = "Gray";
    distance[indexVertex] = 0;
    Queue.append(indexVertex)

    while(len(Queue)>0):
        vertex = Queue.pop(0);
        for j in range(len(graph[vertex])):
            if (graph[vertex][j]==1):
                if (color[j] == "White"):
                    Queue.append(j);
                    print ("Node "+str(j+1));
                    distance[j] = distance[vertex]+1
                    color[j] = "Gray";
            color[vertex]= "black"

    return distance[end-1]
        



cases = int(raw_input());
#print cases


while(cases>0):
        
    inputs = raw_input();
    num  = map(int,inputs.split(" "));
    vertex = int(num[0]);
    edges = int(num[1]);
    #print vertex
    #print edges

    aMatrix = [[0]*vertex for x in range(vertex)];
    #print aMatrix
    for i in range(edges):
        fromVertex,toVertex = map(int,raw_input().split());
        #print fromVertex,toVertex
        #fromVertex  = int(edge[0]);
        #toVertex = int(edge[1]);
        aMatrix[fromVertex-1][toVertex-1] = 1;
        
    #print aMatrix;   
    start = int(raw_input());
    end =  int(raw_input());
    print bfs(aMatrix,start)
    cases -= 1;
    
     

