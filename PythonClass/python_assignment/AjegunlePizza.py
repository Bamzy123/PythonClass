import math

def calculate_order(order_number, order_type):
    pizza_types = {
        1: {"name": "Sapa size", "slices": 4, "price": 2500},
        2: {"name": "Small Money", "slices": 6, "price": 2900},
        3: {"name": "Big boys", "slices": 8, "price": 4000},
        4: {"name": "Odogwu", "slices": 12, "price": 5200},
    }

    if order_type not in pizza_types:
        raise ValueError("Invalid pizza type selected.")

    selected_pizza = pizza_types[order_type]

    slices_per_box = selected_pizza["slices"]

    price_per_box = selected_pizza["price"]

    number_of_boxes = math.ceil(order_number / slices_per_box)

    leftovers = (number_of_boxes * slices_per_box) - order_number

    total_price = number_of_boxes * price_per_box

    return {
        "pizza_name": selected_pizza["name"],

        "price_per_box": price_per_box,

        "number_of_boxes": number_of_boxes,

        "leftovers": leftovers,

        "total_price": total_price,
    }

def ajegunle_pizza():

    print("Welcome to Iya Moses Pizza joint, Ajegunle. \n \n We sell the best and most affordable pizzas in town!")

    order_number = -1
    while order_number < 0:
        try:
            order_number = int(input("\nEnter the number of people you would like to order for (Each person gets 1 slice of pizza): "))
            if order_number < 0:
                print("Invalid Input, please enter a valid number.")
        except ValueError:
            print("Invalid Input. Please enter a number.")

    print("\nBelow is the information on the types of Pizza we have and their prices. Look through carefully: \n ")

    print("Pizza Type\t\tNumber of Slices\tPrice Per Box \n ")

    print("1. Sapa size\t\t4\t\t\t2,500")
    print("2. Small Money\t\t6\t\t\t2,900")
    print("3. Big boys\t\t8\t\t\t4,000")
    print("4. Odogwu\t\t12\t\t\t5,200\n")

    order_type = -1
    while order_type < 1 or order_type > 4:
        try:
            order_type = int(input("Select a number corresponding to the pizza type you would like to order: "))
            if order_type < 1 or order_type > 4:
                print("Invalid Order Type. Enter a valid number from the chart above.")
        except ValueError:
            print("Invalid Input, please enter a number.")

    result = calculate_order(order_number, order_type)

    print(f"\nYou ordered for the {result['pizza_name']} pizza costing {result['price_per_box']} per box.")

    print(f"Number of boxes of pizza to buy: {result['number_of_boxes']} boxes")

    print(f"Number of leftover slices after serving: {result['leftovers']} slices") 

    print(f"Total price: {result['total_price']} Naira")

ajegunle_pizza()