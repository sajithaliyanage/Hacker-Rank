num = int(raw_input())
userIn =[num]
userIn= raw_input().split(" ")

string = ""
for i in range(len(userIn)-1,-1,-1):
    string +=  userIn[i];
    string += " ";

print string
