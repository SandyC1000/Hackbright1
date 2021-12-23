"""Classes for melon orders."""
class AbstractMelonOrder:
    """An Abrstract melon order."""

    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
#        self.country_code = country_code
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price *= 1.5 

        total = (1 + self.tax) * self.qty * base_price

        

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type="domestic", tax=0.08)
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type="international", tax=0.17)
        self.country_code = country_code


    def get_total(self):
        total = super().get_total()

        return total + 3 if self.qty < 10 else total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """An Government (US) melon order."""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type="Government", tax=0.0)
        #super().__int__(species, qty, "governemnt", 0.0)
        self.passed_inspection = "False"
    

    def mark_inspection(self, passed):
        """Mark if isnpection passed."""

        self.passed_inspection = passed


# domestic_order = DomesticMelonOrder("cantaloupe", 8)
# print("domestic_order species = ", domestic_order.species)
# print("domestic_order qty = ", domestic_order.qty)
# print("domestic_order order_type = ", domestic_order.order_type)
# print("domestic_order tax = ", domestic_order.tax)
# print("domestic_order shipped = ", domestic_order.shipped)
# print(domestic_order.get_total())
# print()
# int_order = InternationalMelonOrder("watermelon", 6, "AUS" )
# print("int_order species = ", int_order.species)
# print("int_order qty = ", int_order.qty)
# print("int_order order_type = ", int_order.order_type)
# print("int_order tax = ", int_order.tax)
# print("int_order shipped = ", int_order.shipped)
# print("int_order country_code = ", int_order.country_code)
# print(int_order.get_total())


gov_order = GovernmentMelonOrder("watermelon", 6)
print("gov_order species = ", gov_order.species)
print("gov_order qty = ", gov_order.qty)
print("gov_order order_type = ", gov_order.order_type)
print("gov_order shipped = ", gov_order.shipped)
print("gov_order passed inspection = ", gov_order.passed_inspection)
print(gov_order.get_total())
gov_order.mark_inspection(False)
print("gov_order passed inspection = ", gov_order.passed_inspection)
gov_order.mark_inspection(True)
print("gov_order passed inspection = ", gov_order.passed_inspection)
