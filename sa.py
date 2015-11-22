class Node:
    def __init__(self,data):
        self.data = data;
        self.next=None;

    def __str__(self):
        return str(self.data)


v1_1 = Node(4);
v2_1 = Node(1);
v3_1 = Node(1);
v4_1 = Node(1);
v5_1 = Node(4);

v3_2 = Node(5);
v3_3 = Node(2);
v5_2 = Node(3);

v3_1.next = v3_2;
v3_2.next = v3_3;
v5_1.next = v5_2;


adje_list = [v1_1,v2_1,v3_1,v4_1,v5_1];

