choice = input("Please enter your type of expense: food, cinema, loan, trip, transportation, others: ")
if choice == "food":
    food = []

    n = int(input("How many entries do you wish to have in food category: "))

    for i in range(n):
        expense = float(input(f"Enter expense {i+1}: "))
        food.append(expense)

    print("\nFood Expenses:")
    print(food)

    total1 = sum(food)
    print(f"Total Food Expense: ₹{total1}")
    
if choice == "cinema":
    cinema = []

    n = int(input("How many entries do you wish to have in cinema category: "))

    for i in range(n):
        expense = float(input(f"Enter expense {i+1}: "))
        cinema.append(expense)

    print("\nCinema Expenses:")
    print(cinema)

    total2 = sum(cinema)
    print(f"Total Cinema Expense: ₹{total2}")
    
if choice == "loan":
    loan = []

    n = int(input("How many entries do you wish to have in loan category: "))

    for i in range(n):
        expense = float(input(f"Enter expense {i+1}: "))
        loan.append(expense)

    print("\nLoan Expenses:")
    print(loan)

    total3 = sum(loan)
    print(f"Total Loan Expense: ₹{total3}")
    
if choice == "trip":
    trip = []

    n = int(input("How many entries do you wish to have in trip category: "))

    for i in range(n):
        expense = float(input(f"Enter expense {i+1}: "))
        trip.append(expense)

    print("\nTrip Expenses:")
    print(trip)

    total4 = sum(trip)
    print(f"Total Trip Expense: ₹{total4}")
    
if choice == "transportation":
    transportation = []

    n = int(input("How many entries do you wish to have in transportation category: "))

    for i in range(n):
        expense = float(input(f"Enter expense {i+1}: "))
        transportation.append(expense)

    print("\nTransportation Expenses:")
    print(transportation)

    total5 = sum(transportation)
    print(f"Total Transportation Expense: ₹{total5}")
    
if choice == "others":
    others = []

    n = int(input("How many entries do you wish to have in others category: "))

    for i in range(n):
        expense = float(input(f"Enter expense {i+1}: "))
        others.append(expense)

    print("\nOther Expenses:")
    print(others)

    total6 = sum(others)
    print(f"Total Food Expense: ₹{total6}")
    
print(f"Thanks for using mate!! Have a great day with less expenses 🤝")