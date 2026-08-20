students=["Bashir","Aisha","Bashir","Sara","Aisha","Bashir"]
count={}
for name in students:
    if name in count:
        count[name]+=1
    else:
        count[name]=1
print(count)