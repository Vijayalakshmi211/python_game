class Drink:
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost


class CoffeeMachine:
    def __init__(self):
        self.menu = {
            "expresso": Drink("expresso", {"water": 50, "coffee": 18}, 1.5),
            "latte": Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            "cappuccino": Drink("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.5),
        }
        self.resources = {"water": 300, "milk": 200, "coffee": 100}
        self.profit = 0

    def is_resource_sufficient(self, ingredients):
        return all(ingredients[item] <= self.resources[item] for item in ingredients)

    def process_coins(self):
        print("Please insert coins")
        return sum(int(input(f"How many {coin}? ")) * value for coin, value in 
                   [("quarters", 0.25), ("dimes", 0.10), ("nickels", 0.05), ("pennies", 0.01)])

    def is_transaction_successful(self, payment, cost):
        if payment >= cost:
            self.profit += cost
            change = round(payment - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        print("Sorry, that's not enough money. Money refunded.")
        return False

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕. Enjoy!")

    def report(self):
        print(f"Water: {self.resources['water']}ml.\nMilk: {self.resources['milk']}ml.\nCoffee: {self.resources['coffee']}g.\nMoney: ${self.profit}")

    def run(self):
        while True:
            choice = input("What would you like? (expresso/latte/cappuccino): ").lower()
            if choice == "off":
                break
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                drink = self.menu[choice]
                if self.is_resource_sufficient(drink.ingredients):
                    payment = self.process_coins()
                    if self.is_transaction_successful(payment, drink.cost):
                        self.make_coffee(drink)
                else:
                    print("Sorry, there are not enough resources to make your drink.")
            else:
                print("Invalid choice, please select a valid drink.")


if __name__ == "__main__":
    CoffeeMachine().run()