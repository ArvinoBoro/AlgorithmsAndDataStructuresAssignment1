from matrix import Matrix

def main():
    print("\nWelcome to Arvin's Advanced Shopping-Data Management System.", end='')
    while True:
        print("""            
1. Load Product Data
2. Display Product Data
3. Insert 
4. Update 
5. Delete 
6. Search 
7. Sort by Price
0. Quit""")
        user_option = int(input("Select an option: "))

        if user_option == 0: # Quit
            break

        elif user_option == 1: # Load Product Data
            matrix = Matrix("product_data.txt")

        elif user_option == 2: # Display Product Data
            if 'matrix' in locals():
                print(f"\n{matrix}")
            else:
                print("Error: Data must be loaded first.")

        elif user_option == 3: # Insert 
            if 'matrix' in locals():
                while True:
                    try:
                        position = int(input("Insertion position: "))
                        if position < matrix.get_entry_length() and position > 1:   
                            break
                        else:
                            print("Error: The insertion position is out of bounds.")
                    except ValueError:
                        print("Error: The insertion position is not an integer.")
                print(f"Enter the attributes of the product. A name and valid price must be entered. The category and identifier can be left blank with the return key.")
                while True:
                    name = str(input("Name: "))
                    if not name == '':
                        break

                while True:
                    try:
                        price = str(input("Price: "))
                        float(price)
                        break
                    except ValueError:   
                        print("Error: Price must be an integer or float.")

                category = str(input("Category: "))
                identifier = str(input("ID: "))
                if matrix.insert(position, identifier, name, price, category):
                    print("Product insertion successful.")
            else:
                print("Error: Data must be loaded first.")

        elif user_option == 4: # Update 
            if 'matrix' in locals():
                line_number = int(input("Product line number: "))
                print(f"Enter the new attributes of product {line_number}. A valid price must be entered. All other attributes can be left unchanged by entering 'NO'.\n")
                name = str(input("Name: "))
                while True:
                    try:
                        price = str(input("Price: "))
                        float(price)
                        break
                    except ValueError:
                        print("Price must be an integer or float.")
                category = str(input("Category: "))
                identifier = str(input("ID: "))
                
                if matrix.update(line_number, identifier, name, price, category):
                    print("Product update succesful.") 
            else: 
                print("Error: Data must be loaded first.")

        elif user_option == 5: 
            if 'matrix' in locals():
                line_number = int(input("Line number: "))
                if matrix.delete(line_number):
                    print("Product deletion successful.")
            else: 
                print("Error: Data must be loaded first.")

        elif user_option == 6: 
            if 'matrix' in locals():
                print('''0. No Attribute
1. ID
2. Name
3. Price
4. Category''')            
                while True:
                    try:
                        attribute_type = int(input("Enter the attribute type number: "))
                        if attribute_type > -1 and attribute_type < 5:
                            break
                        else:
                            print("Error: Input must be an integer from 0 to 4.")
                    except ValueError:
                        print("Error: Input must be an integer from 0 to 4.")  
                value = str(input("Enter the attribute value: "))
                results = matrix.search(attribute_type, value)
                if results:
                    for result in results:
                        print(f"Entry found at: {result}")
                else:
                    print("No entries found.")
            else: 
                print("Error: Data must be loaded first.")

        elif user_option == 7: # Sort
            if 'matrix' in locals():
                if matrix.bubble_sort(2):
                    print("Product data sorted successfuly.")     
            else: 
                print("Error: Data must be loaded first.")
        else: 
            print("Error: Invalid input.\n")

if __name__=='__main__': 
    main()