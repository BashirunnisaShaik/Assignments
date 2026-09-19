def vowels(s):
    c=0
    for i in s:
        if i in "aeiouAEIOU":
            c=c+1
    return c

print(vowels("Bashir"))