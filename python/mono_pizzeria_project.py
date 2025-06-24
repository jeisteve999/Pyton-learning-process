# Initialization of variables
money = float(input("How much money do you have"))
initial_money= money
total = 0 
order = []

# Prices

hawaiian_pizza = 15.2
chicken_pizza = 10.3
mushroom_pizza = 17.35
extra_cheese = 5.4
extra_ham = 8.1
extra_pineapple = 6.8

# Welcome message
print("\nWelcome to El Mono Pizzeria \n")

# --- Pizza selection ---
while True:
    print(f"1. Hawaiian Pizza: ${hawaiian_pizza}")
    print(f"2. Chicken Pizza: ${chicken_pizza}")
    print(f"3. Mushroom Pizza: ${mushroom_pizza}")
    choice = int(input("Please choose your pizza (1, 2, or 3): "))

    match choice:
        case 1:
            print(f"You selected Hawaiian Pizza. Cost: ${hawaiian_pizza}")
            total += hawaiian_pizza
            money -= hawaiian_pizza
            print(f"Remaining balance: ${round(money, 2)}")
            order.append(f"Hawaiian Pizza - ${hawaiian_pizza}")
            break
        case 2:
            print(f"You selected Chicken Pizza. Cost: ${chicken_pizza}")
            total += chicken_pizza
            money -= chicken_pizza
            print(f"Remaining balance: ${round(money, 2)}")
            order.append(f"Chicken Pizza - ${chicken_pizza}")
            break
        case 3:
            print(f"You selected Mushroom Pizza. Cost: ${mushroom_pizza}")
            total += mushroom_pizza
            money -= mushroom_pizza
            print(f"Remaining balance: ${round(money, 2)}")
            order.append(f"Mushroom Pizza - ${mushroom_pizza}")
            break
        case _:
            print("Invalid option. Please choose 1, 2, or 3.")

# --- Extra ingredients ---
while True:
    print("\nWould you like to add any extra ingredients?")
    print(f"1. Cheese - ${extra_cheese}")
    print(f"2. Ham - ${extra_ham}")
    print(f"3. Pineapple cubes - ${extra_pineapple}")
    print("4. No extra ingredients")

    extra_choice = int(input("Please select an option (1 to 4): "))

    match extra_choice:
        case 1:
            print(f"You added extra cheese. Cost: ${extra_cheese}")
            total += extra_cheese
            money -= extra_cheese
            print(f"Remaining balance: ${round(money, 2)}")
            order.append(f"Extra Cheese - ${extra_cheese}")
            break
        case 2:
            print(f"You added extra ham. Cost: ${extra_ham}")
            total += extra_ham
            money -= extra_ham
            print(f"Remaining balance: ${round(money, 2)}")
            order.append(f"Extra Ham - ${extra_ham}")
            break
        case 3:
            print(f"You added pineapple cubes. Cost: ${extra_pineapple}")
            total += extra_pineapple
            money -= extra_pineapple
            print(f"Remaining balance: ${round(money, 2)}")
            order.append(f"Pineapple Cubes - ${extra_pineapple}")
            break
        case 4:
            print("No extra ingredients added. Thank you.")
            break
        case _:
            print("Invalid option. Please choose 1 to 4.")

# --- Payment summary ---
print("\n--- Receipt ---")
if total <= initial_money:
    print(f"Total cost: ${round(total, 2)}")
    print(f"Change: ${round(initial_money - total, 2)}")
    print("Your order:")
    for item in order:
        print(f"- {item}")
    print("\nThank you for your purchase!")
else:
    print("Insufficient funds. Please add more money.")

