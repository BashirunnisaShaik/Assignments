try:
    a=float(input("Enter attendance: "))
    if a<75:
        raise ValueError("Attendance is below 75%")
    print("Eligible")
except ValueError as e:
    print(e)