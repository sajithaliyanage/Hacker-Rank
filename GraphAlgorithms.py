'''
Created on April 3, 2014

Demonstration of some simple graph algorithms.
    
'''

import sys

'''
Reads in the specified input file containing
adjacent edges in a graph and constructs an
adjacency list.

The adjacency list is a dictionary that maps
a vertex to its adjacent vertices.
'''
def init(fileName): 
    
    graphFile = open(fileName)

    '''
    create an initially empty dictionary representing
    an adjacency list of the graph
    '''
    adjacencyList = { }
    
    '''
    collection of vertices in the graph (there may be duplicates)
    '''
    vertices = [ ]

    for line in graphFile:
        '''
        Get the two vertices
        
        Python lets us assign two variables with one
        assignment statement.
        '''
        (firstVertex, secondVertex) = line.split()
        
        '''
        Add the two vertices to the list of vertices
        At this point, duplicates are ok as later
        operations will retrieve the set of vertices.
        '''
        vertices.append(firstVertex)
        vertices.append(secondVertex)

        '''
        Check if the first vertex is in the adjacency list.
        If not, add it to the adjacency list.
        '''
        if firstVertex not in adjacencyList:
            adjacencyList[firstVertex] = [ ]

        '''
        Add the second vertex to the adjacency list of the first vertex.
        '''
        adjacencyList[firstVertex].append(secondVertex)

    '''
    Woah, here Python is letting us return two values from this function!
    '''
    return (vertices,adjacencyList)


'''
Begins the DFS algorithm.
'''
def DFSInit(vertices, adjacencyList):
    
    print 'DFS Traversal'

    # creates a set of vertices (removes duplicates)
    setOfVertices = set(vertices)
    
    # initially all vertices are considered unknown
    unknownVertices = set(vertices)
    
    '''
    Your logic will go here
    '''


'''
depth-first traversal of specified graph

This is likely the function representing the recursive portion
of the DFS algorithm
'''
def DFS():
    pass
    
        
if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print 'Usage python GraphAlgorithms.py [input file]'
        quit()
        
    (vertices,adjacencyList) = init(sys.argv[1])
    
    # Construct a depth-first search
    DFSInit(vertices, adjacencyList)

    '''
    don't forget the BFS algorithm!
    '''

