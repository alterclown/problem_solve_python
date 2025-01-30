a = 10
b = 20

def func():
    global a
    global b
    a = 25
    b = b
    c = 2+3j
    print("a:",a,"b:",b,"c:",type(c))

result = func()