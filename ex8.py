# Nested condition -> form one step to another
marks = int(input("Enter Msrks"))
if marks >= 0 and marks <= 100 :
    if marks > 90:
        print("A")

    elif marks > 80:
        print("B")

    elif marks > 70:
        print("C")

    else:
        print("D")
else: print("Invaild marks")
