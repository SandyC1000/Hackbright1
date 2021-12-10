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
 

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



# domestic_order = DomesticMelonOrder("watermelon", 6)
# print("domestic_order species = ", domestic_order.species)
# print("domestic_order qty = ", domestic_order.qty)
# print("domestic_order order_type = ", domestic_order.order_type)
# print("domestic_order tax = ", domestic_order.tax)
# print("domestic_order shipped = ", domestic_order.shipped)


# int_order = InternationalMelonOrder("cantaloup", 2, "AUS" )
# print("int_order species = ", int_order.species)
# print("int_order qty = ", int_order.qty)
# print("int_order order_type = ", int_order.order_type)
# print("int_order tax = ", int_order.tax)
# print("int_order shipped = ", int_order.shipped)
# print("int_order country_code = ", int_order.country_code)
