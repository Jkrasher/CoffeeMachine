

from main import MENU, resources

# print(MENU["espresso"])
# print(MENU["latte"])
# print(MENU["cappuccino"])
# print(MENU)
# print(resources)





# TODO: 5. Process coins.
#           a. If there are sufficient resources to make the drink selected, then the program should
#               prompt the user to insert coins.
#           b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#           c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#               pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: 6. 6. Check transaction successful?
#           a. Check that the user has inserted enough money to purchase the drink they selected.
#               E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#               program should say “ Sorry that's not enough money. Money refunded. ”.
#           b. But if the user has inserted enough money, then the cost of the drink gets added to the
#               machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#               Water: 100ml
#               Milk: 50ml
#               Coffee: 76g
#               Money: $2.5
#           c. If the user has inserted too much money, the machine should offer change.
#
#
# TODO: 7. Make Coffee.
#           a. If the transaction is successful and there are enough resources to make the drink the
#               user selected, then the ingredients to make the drink should be deducted from the
#               coffee machine resources.
#               E.g. report before purchasing latte:
#               Water: 300ml
#               Milk: 200ml
#               Coffee: 100g
#               Money: $0
#               Report after purchasing latte:
#               Water: 100ml
#               Milk: 50ml
#               Coffee: 76g
#               Money: $2.5
#           b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#               latte was their choice of drink.

# TODO: 1. Print Report of Resources
# When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
#           a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#           the machine. Your code should end execution when this happens.


# TODO: 3. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
#           a. Check the user’s input to decide what to do next.
#           b. The prompt should show every time action has completed, e.g. once the drink is
#           dispensed. The prompt should show again to serve the next customer.


totalMoneyEarned = 0


def is_resources_enough(order_ingredients):
    """Returns True when order can be made, False if ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins -->")
    total = int(input("How many quarters are you paying with?")) * 0.25
    total += int(input("How many dimes are you paying with?")) * 0.10
    total += int(input("How many nickels are you paying with?")) * 0.05
    total += int(input("How many pennies are you paying with?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """ Return True when the payment is accepted or False if money is not enough."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 3)
        print(f" Here is ${change} dollars in change.")
        global totalMoneyEarned
        totalMoneyEarned += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_Coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources when enough resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f" Here is your {drink_name} ☕️")

is_on = True

while is_on:
    order = input("What would you like? (espresso / latte / cappuccino): ")
    if order == "off":
        print("<<*** --- Entering diagnostics mode --- ***>>")
        is_on = False
    elif order == "report":
        print ( "\n", f"Water: {resources['water']}ml", "\n",
                f"Milk: {resources['milk']}ml", "\n",
                f"Coffee: {resources['coffee']}g")
        print(f" Money Earned: ${(round(totalMoneyEarned, 3))}", "\n")

    else:
        drink = MENU[order]
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_Coffee(order, drink["ingredients"])







        # print(drink, resourceValues)
        # for ingred in drink.keys():
        #     print(ingred)
        #     for res in resources.keys():
        #         print(res, " + ", ingred)
        #         if ingred == res:
        #             print(drink.values)
        #
        #         else:
        #             print("Not a match")

            # TODO: 4. Check resources sufficient?
            #           a. When the user chooses a drink, the program should check if there are enough
            #               resources to make that drink.
            #           b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
            #               not continue to make the drink but print: “ Sorry there is not enough water. ”
            #           c. The same should happen if another resource is depleted, e.g. milk or coffee.


            # if ((drink.values()) - (resources.values()) < 0):
            #     Print("Sorry there isn't enough resources for that drink.")
            # else:
            #     print("Totally enough Bro!")



    # if order in MENU:
    #     if order == MENU[]





# def ingredients_list():
#     ingredientValues = []
#     ingredients_are = MENU[str(order)]["ingredients"]
#     ingredient_list = [key for key in ingredients_are]
#     #ingredient 1
#     ingredient1 = ingredient_list[0]
#     print("ingredient1: ", ingredient1)
#     ingredient1_value = [value for value in ingredients_are.values()][0]
#     print("Ingredient1 Value: ", ingredient1_value)
# # add in boolean check for correct ingredient milk vs coffe for ingredients 2 & 3
#
#     # ingredient 2
#     ingredient2 = ingredient_list[1]
#     print("ingredient2: ", ingredient2)
#     ingredient2_value = [value for value in ingredients_are.values()][1]
#     print("Ingredient2 Value: ", ingredient2_value)
#
#     # ingredient 3
#     ingredient3 = ingredient_list[2]
#     print("ingredient3: ", ingredient3)
#     ingredient3_value = [value for value in ingredients_are.values()][2]
#     print("Ingredient3 Value: ", ingredient3_value)
#
#     return ingredient_list, ingredientValues







# print(MENU[str(order)], "\n", "\n", "Begin Program Calulations:", "\n")

# def use_resources():

# reduce_water = (resources["water"]) - (MENU[str(order)]["ingredients"]["water"])
# print(reduce_water)
#
# reduce_milk = (resources["milk"]) - (MENU[str(order)]["ingredients"]["milk"])
# print(reduce_milk)
#
# reduce_coffee = (resources["coffee"]) - (MENU[str(order)]["ingredients"]["coffee"])
# print(reduce_coffee)





# if (MENU[str(order)]):
#     print((MENU[str(order)]["ingredients"]["water"]))
#     print((MENU[str(order)]["cost"]))
#     print(MENU[str(order)]["ingredients"])
#
# else:
#     print("Oops!!")
