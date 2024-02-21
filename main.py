import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
machine = SandwichMaker(resources)
cashier = Cashier()


def main():
    while True:
        order = input("What would you like? (small/medium/large/off/report): ")
        match order:
            case "small" | "medium" | "large":
                # Check resources
                if not machine.check_resources(recipes[order]["ingredients"]):
                    continue

                # Process Coins
                if not cashier.transaction_result(cashier.process_coins(), recipes[order]["cost"]):
                    continue

                # Make Sandwich
                machine.make_sandwich(order, recipes[order]["ingredients"])

            case "off":
                break
            case "report":
                print("Bread: " + str(machine.machine_resources["bread"]) + " slice(s)\n" +
                      "Ham: " + str(machine.machine_resources["ham"]) + " slices(s)\n" +
                      "Cheese: " + str(machine.machine_resources["cheese"]) + " pound(s)")


if __name__=="__main__":
    main()
