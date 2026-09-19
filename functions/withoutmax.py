def largest(a):
    l=a[0]
    for i in a:
        if i>l:
            l=i
    return l

print(largest([10,25,15,40,20]))