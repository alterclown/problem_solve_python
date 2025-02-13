def Array_abc(char):
    for i in range(len(char) - 2):
        print(char[i])
        if char[i] == 'a' and char[i + 1] == 'b' and char[i + 2] == 'c':
            return True
    return False


print (Array_abc(['a', 'x', 'a', 'b', 'c']))