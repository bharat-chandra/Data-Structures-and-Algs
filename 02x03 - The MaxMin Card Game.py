This card game begins with an empty deck.

There are following types of operations in the game :
Add X : Add a card with number X onto the top of the deck pile.
Remove : Remove the TopMost card from the deck pile.
CallMin : Find the minimum numbered card from the deck pile.
CallMax : Find the maximum numbered card from the deck pile.

You are given a sequence of operations of the game and your task is to write a program to play the game.

NOTE : You are expected to use the stack data structure only to get optimal solution. Other solutions may not be efficient enough.

INPUT

First line contains N the number of operations.
Next N lines each contain one operation each : "Add X", "Remove", "CallMax" or "CallMin" where X can be any non-negative integer.

OUTPUT

Output the minimum element whenever CallMin command is given, the maximum element whenever CallMax command is given, or "Invalid" whenever CallMin/CallMax/Remove command is given on an empty stack.

Sample Input 0

15
Add 1
Add 2
Add 3
CallMin
CallMax
Add 0
CallMin
CallMax
Remove
Remove
CallMin
Remove
Remove
Remove
CallMax
Sample Output 0

1
3
0
3
1
Invalid
Invalid



items = []
for i in range(int(input())):
    a=input()
    if a[0:3] == 'Add':
        x,b=a.split()
        b = int(b)
        items.append(b)
    elif a[0:6] == 'Remove':
        if(len(items) == 0):
            print('Invalid')
        else:
            items.pop()
    elif a[0:7] == 'CallMin':
        if(len(items) == 0):
            print('Invalid')
        else:
            print(min(items))
    elif a[0:7] == 'CallMax':
        if(len(items) == 0):
            print('Invalid')
        else:
            print(max(items))
