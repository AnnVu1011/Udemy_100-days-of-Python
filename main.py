from data import MENU, RESOURCES, COINS

# Function to check if the machine resources have enough to make user's coffee choice
def resources_check(coffee_resources, total_resources):
    for resource in total_resources:
        check = total_resources[resource] - coffee_resources[resource]
        # print(f"Total {resource} = {total_resources[resource]}, Coffe needs: {coffee_resources[resource]}, Left = {check}")
        if check < 0:
            print(f"Sorry there is not enough {resource}")
            return False
    return True

# Function to update machine total resources
def update_resources(coffee_resources, total_resources):
    left_resouces = {}
    for resource in total_resources:
        left_resouces[resource] = total_resources[resource] - coffee_resources[resource]
    return left_resouces

# MAIN OPERATOR
machine_using = True
total_earned_money = 0

while machine_using:
    # Ask for user's coffee choice and save coffee needed ingredients
    user_choice = str(input("What would you like? (espresso/latte/cappuccino/report/off): ")).lower()
    if user_choice == "off": # Turn off the Coffee Machine
        print("See you again!")
        machine_using = False
    elif user_choice == "report": # Print report about machine's left resources and total money earned
        print("Coffee machine has left:")
        print(f"Water: {total_water}")
        print(f"Milk: {total_milk}")
        print(f"Coffee: {total_coffee}")
        print(f"Total earned money: {total_earned_money}")
    else:
        user_choice_resources = {
            "water": MENU[user_choice]["ingredients"]["water"],
            "coffee": MENU[user_choice]["ingredients"]["coffee"]
        }
        if user_choice == "espresso":
            user_choice_resources["milk"] = 0
        else:
            user_choice_resources["milk"] = MENU[user_choice]["ingredients"]["milk"]
        print(f"Your coffee choice needs: {user_choice_resources} and it costs {MENU[user_choice]["cost"]}")

    # Check resources sufficient
    can_make_coffee = resources_check(user_choice_resources,RESOURCES)
    print(f"Can make coffee = {can_make_coffee}")
    print(f"Resources before purchasing: {RESOURCES}")

    if can_make_coffee:
        # Process coins
        print("Please insert coins.")
        num_paid_quarter = int(input("How many quarters?: "))
        num_paid_dime = int(input("How many dimes?: "))
        num_paid_nickle = int(input("How many nickles?: "))
        num_paid_penny = int(input("How many pennies?: "))
        user_paid = num_paid_quarter * COINS["quarter"] + num_paid_dime * COINS["dime"] + num_paid_nickle * COINS["nickel"] + num_paid_penny * COINS["penny"]
        print(f"You have paid: ${user_paid}")

        coffee_cost = MENU[user_choice]["cost"]
        print(f"Coffee costs: ${coffee_cost}")

        # Check transaction successful
        user_change = round((user_paid - coffee_cost),2)
        transaction_success = True
        if user_change < 0:
            print("Sorry that's not enough money. Money refunded")
            transaction_success = False
        else:
            print(f"Here is ${user_change} dollars in change.")
            total_earned_money += coffee_cost

        # If the transaction is made, update machine resources
        if transaction_success == True:
            print(f"Here is your {user_choice}. Enjoy!")
            RESOURCES = update_resources(user_choice_resources,RESOURCES)
            print(f"Machine resources left = {RESOURCES}, total earned = {total_earned_money}")
    else:
        resources_refill = str(input("The Machine resources is running low, do you want to reset it? Please insert 'y' or 'n': "))
        if resources_refill == 'y':
            RESOURCES["water"] = 300
            RESOURCES["milk"] = 200
            RESOURCES["coffee"] = 100

