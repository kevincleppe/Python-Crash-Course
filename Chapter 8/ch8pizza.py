def make_pizza(size, *toppings):
    print(f"Making a {size} sized pizza with the following things: ")
    for i in toppings:
        print(f"- {i}")


make_pizza(16, "saus", "peppe")