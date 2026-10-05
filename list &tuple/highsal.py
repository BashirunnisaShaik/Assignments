employees=[("Bashir","Developer",50000),("Aisha","Tester",45000),("Sara","Manager",70000)]
highest=employees[0]
for e in employees:
    if e[2]>highest[2]:
        highest=e
print(highest)