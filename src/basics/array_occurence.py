def array_occurence():
    count = 0
    arr = [1, 2, 3, 4, 2, 2, 5, 6, 2]
    target = 2
    for item in arr:
        if item == target:
            print(item)
            count += 1

    print(count)

result = array_occurence()

