import copy
DEFAULT_INITIAL_BASKET = ["orange", "apple"]

def create_picnic_basket(healthy1, hungry, initial_basket=DEFAULT_INITIAL_BASKET):
    basket = copy.deepcopy(initial_basket)
    if healthy1:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket

# Reproducer
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True))
print("Third basket:", create_picnic_basket(True, True,DEFAULT_INITIAL_BASKET))

print("WHY DO I HAVE 2 STRAWBERRIES WHEN I AM HEALTH AND HUNGRY?")