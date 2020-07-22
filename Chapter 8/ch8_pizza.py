def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for i in toppings:
        print(f"- {i}")
