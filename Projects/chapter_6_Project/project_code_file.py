# Initialize inventory as a dictionary
inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add New Product")
    print("2. Update Stock Levels")
    print("3. View Products by Category")
    print("4. Generate Low Stock Report")
    print("5. Search for Products")
    print("6. View All Products")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        # Add New Product
        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))
        stock_quantity = int(input("Enter Stock Quantity: "))
        inventory[product_id] = (product_id, name, category, price, stock_quantity)
        print("Product added successfully.")

    elif choice == '2':
        # Update Stock Levels
        product_id_to_update = int(input("Enter Product ID to update: "))
        if product_id_to_update in inventory:
            new_stock_level = int(input("Enter new Stock Quantity: "))
            product = inventory[product_id_to_update]
            updated_product = (product[0], product[1], product[2], product[3], new_stock_level)
            inventory[product_id_to_update] = updated_product
            print("Stock level updated successfully.")
        else:
            print("Product ID not found.")

    elif choice == '3':
        # View Products by Category
        category_to_view = input("Enter Category to view: ")
        found = False
        print(f"\nProducts in category '{category_to_view}':")
        for product_id in inventory:
            product = inventory[product_id]
            if product[2] == category_to_view:
                print(product)
                found = True
        if not found:
            print("No products found in this category.")

    elif choice == '4':
        # Generate Low Stock Report
        low_stock_threshold = int(input("Enter low stock threshold: "))
        found = False
        print(f"\nLow Stock Report (Threshold: {low_stock_threshold}):")
        for product_id in inventory:
            product = inventory[product_id]
            if product[4] < low_stock_threshold:
                print(product)
                found = True
        if not found:
            print("No products found below the stock threshold.")

    elif choice == '5':
        # Search for Products
        search_term = input("Enter Product Name or ID to search: ")
        found = False
        print(f"\nSearch Results for '{search_term}':")
        for product_id in inventory:
            product = inventory[product_id]
            if str(product[0]) == search_term or product[1].lower() == search_term.lower():
                print(product)
                found = True
        if not found:
            print("No products found with the given name or ID.")

    elif choice == '6':
        # View All Products
        if inventory:
            print("\nAll Products in Inventory:")
            for product_id in inventory:
                print(inventory[product_id])
        else:
            print("No products in the inventory.")

    elif choice == '7':
        # Exit
        print("Exiting the Inventory Management System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
