############
# Part 1   #
############
from typing_extensions import _AnnotatedAlias



class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = [] # set attributes

        # Fill in the rest
        self.code = code
        self.harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        
    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings = self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print(f" - {pairing}")
    return None

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
