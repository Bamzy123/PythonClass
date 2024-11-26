products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Headphones", "price": 100},
]


def display_products(products):

    print("\nAvailable Products:")

    for index, product in enumerate(products, start=1):

        print(f"{index}. {product['name']} - ${product['price']}")

def add_to_cart(cart, products):

    display_products(products)

    selected_product = input("\nEnter the name of the product you want to add: ").strip()


    for product in products:

        if product['name'].lower() == selected_product.lower():

            cart.append(product)

            print(f"{product['name']} has been added to your cart.")
            return

    print("Sorry, that product is not available.")


def remove_from_cart(cart):

    if not cart:

        print("\nYour cart is currently empty!")
        return

    print("\nYour current cart items:")

    for item in cart:

        print(f"- {item['name']} - ${item['price']}")

    item_to_remove = input("\nEnter the name of the product you want to remove: ").strip()

    for product in cart:

        if product['name'].lower() == item_to_remove.lower():

            cart.remove(product)

            print(f"{product['name']} has been removed from your cart.")
            return

    print("The item is currently not in your cart.")


def checkout(cart):

 if not cart:
       	print("\nYour cart is empty. Nothing to checkout.")
        return

 total = sum(item['price'] for item in cart)

 print(f"Thank you for shopping with us! Your total is ${total}.")
 cart.clear()

cart = []

while True:
    print("\nMenu:")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":

        display_products(products)

    elif choice == "2":

        add_to_cart(cart, products)

    elif choice == "3":

        remove_from_cart(cart)

    elif choice == "4":

        if not cart:

            print("\nYour cart is empty!")

        else:
            print("\nYour current cart items:")

            for item in cart:

                print(f"- {item['name']} - ${item['price']}")

    elif choice == "5":

        checkout(cart)

    elif choice == "6":

        print("\nThank you for shopping with us!")

        break
    else:
        print("\nInvalid choice. Please try again.")
