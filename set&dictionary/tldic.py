marks={"Bashir":85,"rukku":92,"nafee":78,"zoya":65,"ayaan":88}
highest=None
lowest=None
topper=None
low_scorer=None
for name in marks:
    if highest is None or marks[name]>highest:
        highest=marks[name]
        topper=name
    if lowest is None or marks[name]<lowest:
        lowest=marks[name]
        low_scorer=name
print("Topper:",topper)
print("Marks:",highest)
print("Lowest:",low_scorer)
print("Marks:",lowest)