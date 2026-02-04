cart = ["apple", "banana", "milk", "bread", "apple", " eggs"]
apple_count = cart.count("apple")
print(f"Number of apples in the cart: {apple_count}")
print(f"Position of Milk: {cart.index("milk")}")
cart.remove("apple")
print(f"Removed item using pop: {cart.pop()}")
print("Is banana in the cart?", "banana" in cart)
print(f"Final cart: {cart}")