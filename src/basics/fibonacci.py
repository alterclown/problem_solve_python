def check_fibonacci(n:int):
    a= 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)




print(check_fibonacci(5))