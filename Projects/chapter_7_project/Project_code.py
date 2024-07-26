# Function to add items to the order
def add_item_to_order(order):
    while True:
        name = input("Enter the item name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        # Validate price input
        price_input = input(f"Enter the price for {name}: ")
        if not price_input.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a valid price.")
            continue
        
        # Validate quantity input
        quantity_input = input(f"Enter the quantity for {name}: ")
        if not quantity_input.isdigit():
            print("Invalid input. Please enter a valid quantity.")
            continue

        # Convert inputs to appropriate types
        price = float(price_input)
        quantity = int(quantity_input)
        
        # Add item to the order
        order.append({'name': name, 'price': price, 'quantity': quantity})
        
    return order

def calculate_total_cost(order, tax_rate=0.07, shipping_cost=5.00):
    subtotal = sum(item['price'] * item['quantity'] for item in order)
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping_cost
    return total, tax, subtotal

def generate_invoice(order, total, tax, subtotal, discount):
    print("\nInvoice:")
    print("----------------------------")
    for item in order:
        print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']}")
    print("----------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Shipping Cost: $5.00")
    if discount:
        print(f"Discount Applied: {discount * 100}%")
    print(f"Total: ${total:.2f}")
    print("----------------------------")


def apply_discount(order, discount_code):
    discount_codes = {'SAVE10': 0.10, 'SAVE20': 0.20, 'SAVE30': 0.30}
    if discount_code in discount_codes:
        discount = discount_codes[discount_code]
    else:
        discount = 0
    if discount:
        for item in order:
            item['price'] -= item['price'] * discount
    return order, discount


order = []
add_item_to_order(order)
if not order:
    print("No items added to the order.")
else:
    discount_code = input("Enter discount code (if any): ").strip().upper()
    order, discount = apply_discount(order, discount_code)
    total, tax, subtotal = calculate_total_cost(order)
    generate_invoice(order, total, tax, subtotal, discount)
