class Stack:
    def __init__(self):
        self.items = [];

    def isEmpty(self):
        return self.items == [];

    def push(self,item):
        self.items.append(item);

    def pop(self):
        return self.items.pop();

    def peek(self):
        return self.items[len(self.items)- 1]

    def size(self):
        return len(self.items);


    def __str__(self):
        return str(self.items);


stack = Stack();
string = "";
name = raw_input();

k = list(name);
print k;

for i in range(len(k)):
    stack.push(k[i]);

for i in range(stack.size()):
    string += stack.pop();

print string;

if(string == name):
    print "Palindrome";

else:
    print "Not a palindrome";
