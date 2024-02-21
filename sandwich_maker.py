
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, resources):
        if self.machine_resources["bread"] < resources["bread"]:
            print("Sorry there is not enough bread.")
            return False
        if self.machine_resources["ham"] < resources["ham"]:
            print("Sorry there is not enough ham.")
            return False
        if self.machine_resources["cheese"] < resources["cheese"]:
            print("Sorry there is not enough cheese.")
            return False
        return True
        """Returns True when order can be made, False if ingredients are insufficient."""

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]

        print(sandwich_size + " sandwich is ready. Bon appetit!")
        """Deduct the required ingredients from the resources.
           Hint: no output"""