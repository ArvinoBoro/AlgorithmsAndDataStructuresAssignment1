class Matrix:
    pass

def main():

    print("\nWelcome to Arvin's Advanced Shopping-Data Mangement System.")
    
    while True:

        print("""\
1. Load Product Data
2. Display Product Data
3. Insert 
4. Update 
5. Delete 
6. Search 
7. Sort 
0. Quit 
        """)

        user_option = int(input("Select an option: "))

        if user_option == 0: # Quit
            break

        elif user_option == 1: # Load product data
            matrix = Matrix()

        elif user_option == 2:
            if 'matrix' in globals():
                #print(matrix)
                pass
            else:
                print("Error: Data must be loaded first")

        elif user_option == 3: # Insert 
            if 'matrix' in globals():
                #position = int(input("Position: "))
                #matrix.insert(position)
                pass

        elif user_option == 4: # Update 
            if 'matrix' in globals():
                #line_number = int(input("Line number: "))
                #matrix.update(line_number)
                pass
            else: 
                print("Error: Data must be loaded first")

        elif user_option == 5: # Delete 
            if 'matrix' in globals():
                #line_number = int(input("Line number: "))
                #matrix.delete(line_number)
                pass
            else: 
                print("Error: Data must be loaded first")

        elif user_option == 6: # Search
            if 'matrix' in globals():
                #search_attribute = 'foo'
                #value = 'bar'
                #matrix.search(search_attribute, value)
                pass
            else: 
                print("Error: Data must be loaded first")

        elif user_option == 7: # Search
            if 'matrix' in globals():
                #matrix.sort()
                pass
            else: 
                print(\n"Error: Data must be loaded first")

        else: 
            print("Error: Invalid input")


if __name__=='__main__': 
    main()