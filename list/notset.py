numbers=[1,2,2,3,4,4,5,5]
new=[]
for n in numbers:
    if n not in new:
        new.append(n)
print(new)