marks={"Bashir":85,"rukku":92,"Sara":78}
highest=None
student=None
for name in marks:
    if highest is None or marks[name]>highest:
        highest=marks[name]
        student=name
print(student)
print(highest)