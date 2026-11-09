#Program to compute the total number of chairs in a class
p = str(input("What is your Problem?"))

if p == "find the total number of chairs in the class":
    r = int(input("What is the number of rows? "))
    c = int(input("How many chairs are in each row? "))
    total = r * c
    print("number of rows is", r)
    print("number of chairs per row is", c)
    print("The total number of chairs in the class is", total)
else:
    print("Invalid input. Please enter 'sum' to calculate the total number of chairs.")
