#Program to compute the weekly expenses of a student
print("This is a weekly expense calculator")
name = input("What is your name?")
dts = float(input("What is your daily transport cost? "))
if dts<0:
    print("Negative values not allowed")
else:
    dfc = float(input("What is your daily feeding cost? "))
if dfc<0:
    print("Negative values not allowed")
else:
    Days = int(input("How many days do you go to school in a week? "))
if Days<0:
    print("Negative values not allowed")
else:
    Extra = float(input("What is your extra expenses? "))
if Extra<0:
    print("Negative values not allowed")
else:
    Ttotal = dts*Days
    Ftotal = dfc*Days
    WTotal = Ttotal + Ftotal + Extra
    print("Here is your WEEKLY EXPENSE SUMMARY")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Student:", name)
    print(f"Transport Total: ₦{Ttotal:.2f}")
    print(f"Feeding Total: ₦{Ftotal:.2f}")
    print(f"Other Expenses: ₦{Extra:.2f}")
    print(f"Weekly Total: ₦{WTotal:.2f}")

    B = int(input("input weekly budget"))
    if B<0:
        print("Budget cannot be negative")
    elif B==WTotal:
        print("Exactly on budget")
    else:
        if B < WTotal:
            print("You are over budget")
        else:
            print("You are within budget")