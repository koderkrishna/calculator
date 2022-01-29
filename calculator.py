a = int(input("enter a number: "))
b = int(input("enter a number: "))
opr = input('''select the operation you want to perform
+ for addition\n- for subtraction\n* for multiplication\n/ for division\nsq for square or\ncube for cube?  ''')
if opr == '+':
    print("sum of two numbers: ", a+b)
elif opr == '-':
    print("subtraction from a to b: ", a-b)
elif opr == '*':
    print("multiplication of two numbers: ", a*b)
elif opr == '/':
    print("dividend and reamainder on division of a by b: ", a/b, a%b)
elif opr == 'sq':
    print("square of a number: ", a*a)
    print("square of a number: ", b*b)
else:
    print("cube of a number: ", a*a*a)
    print("cube of a number: ", b*b*b)