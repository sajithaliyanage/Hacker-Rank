import sys
import os


class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;
        
    def __str__(self):
        return str(self.data);


v1 = Node(4);
v2 = Node(1);
v3 = Node(1);
v4 = Node(1);
v5 = Node(3);

v3_1 = Node(2);
v3_2 = Node(5);
v5_1 = Node(4);

v3.next = v3_1;
v3_1.next = v3_2;
v5.next = v5_1;

adj_list = [v1,v2,v3,v4,v5];

n1 = int(input("Enter first node: "));
n2 = int(input("Enter second node: "));


def isPath(n1,n2):
    p = False;
    n = adj_list[n1-1];
    
    while(n!=None):
        if (n.data == n2):
            print ("There is an edge");
            p = True;
            break;
        n = n.next;

    if(p==False):
        print("There is no edge");
isPath(n1,n2);
 








