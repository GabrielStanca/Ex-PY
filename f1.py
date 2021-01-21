def calculate_list(l):
    b= []
    for n in l:
        if n % 2 == 0:
            b.append(n)
    print(list(b))
    return b

a=[1,4,9,16,25,36,49,64,81,100]
calculate_list(a)
