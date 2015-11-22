userIn = int(raw_input())
lists = []
qw =  ["75025 121393","121393 196418","196418 317811","317811 514229",
"514229 832040","832040 1346269","1346269 2178309 ",
				"2178309 3524578",
				"3524578 5702887",
				"5702887 9227465",
				"9227465 14930352",
				"14930352 24157817",
				"24157817 39088169",
				"39088169 63245986",
				"63245986 102334155"
			]
numZeros = 0;
numofOne =0;
def fib(n):
    if n==0:
        lists.append(0)
        return 0
    elif n==1:
        lists.append(1)
        return 1

    else:
        return fib(n-2)+fib(n-1)

if userIn<=25:
    fib(userIn)

    for i in range(len(lists)):
        if lists[i]==0:
            numZeros +=1;
        elif lists[i] ==1:
            numofOne +=1;

    string = ""
    string += str(numZeros);
    string += str(" ");
    string += str(numofOne);

    print string

else:
    for i in range(41):
        if i+26==userIn:
            print qw[i]
