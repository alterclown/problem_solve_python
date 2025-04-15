def different_list():
    list_1 = ["A", "B", "C",1,2,3]
    list_2 = [1, 2, "A","B"]
    print(list_1)
    print(list_2)
    print(list_1[0])
    print(list_1[0],list_2[1])
    print(list_1[2:5])
    print(list_2[1:])
    print(list_1[2:])
    print(list_2 * 2)
    print(list_1 + list_2)

result = different_list()