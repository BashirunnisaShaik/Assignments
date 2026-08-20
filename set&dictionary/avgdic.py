salary={"Ali":30000,"Sara":40000,"Aisha":35000}
total=0
for s in salary.values():
    total+=s
average=total/len(salary)
print(average)