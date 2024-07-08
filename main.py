class Matrix:
    
    def __init__(self, file_name):
        try:
            fp = open(file_name, 'r+')
        except: 
            print("\nError: File not found.\n")
            return None
        
        self._data_raw = fp.read()
        self._data_organized = []
        self._data_is_sorted = False
        entry = []
        attribute = str()
        
        for i in range(len(self._data_raw)):
                if self._data_raw[i] == '\n':
                    entry.append(attribute.strip())
                    self._data_organized.append(entry)
                    entry = []
                    attribute = ""
                elif self._data_raw[i] == ',' and self._data_raw[i+1] == ' ':
                    i += 1
                    entry.append(attribute.strip())
                    attribute = ""
                else:
                    attribute += self._data_raw[i]
        
        if attribute:
            entry.append(attribute)
            self._data_organized.append(entry)

        print("Data load successful.\n")
    
    def __str__(self):
        entries = ""
        for i in range(len(self._data_organized)):
            entries += f"{i+1}. "
            for j in range(4):
                entries += f" {self._data_organized[i][j]}"
                if j < 3:
                    entries += ','
            entries += '\n'

        return entries
    
    def insert(self, position, *argv):

        if not isinstance(position, int):
            print("Error: The line number is not an integer.\n")
            return None
        
        if not len(argv) == len(self._data_organized[position]):
            return None 

        if position >= len(self._data_organized) or position < 1:
            print("Error: The position is out of range.\n") 
            return None

        self._data_organized.insert(position - 1, argv)
        return 1 

    def update(self, line_number, *argv): # 4
        if not isinstance(line_number, int):
            print("Error: The line number is not an integer.\n")
            return None
        
        if line_number > len(self._data_organized) or line_number < 1:
            print("Error: The line number is out of range.\n")
            return None

        for i in range(len(argv)):
            if not argv[i] == "NO":
                self._data_organized[line_number - 1][i] = argv[i]
        
        return 1


    def delete(self, line_number):  
        if not isinstance(line_number, int):
            print("Error: The line number is not an integer.\n")
            return None

        if line_number > len(self._data_organized) or line_number < 1:
            print("Error: The line number is out of range.\n")
            return None
            
        del self._data_organized[line_number - 1]
        return 1 
    
                         
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
            matrix = Matrix("product_data.txt")

        elif user_option == 2: # Display product data
            if 'matrix' in locals():
                print(f"\n{matrix}")
            else:
                print("Error: Data must be loaded first.\n")

        elif user_option == 3: # Insert 
            if 'matrix' in locals():
                position = int(input("Insertion position: "))
                print(f"Enter the attributes of the product. A name and valid price must be entered. The category and identifier can be left blank with the return key.\n")
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
                    print("Product insertion successful.\n")
            else:
                print("Error: Data must be loaded first.\n")

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
                    print("Product update succesful.\n") 
                
            else: 
                print("Error: Data must be loaded first.\n")

        elif user_option == 5: 
            if 'matrix' in locals():
                line_number = int(input("Line number: "))
                if matrix.delete(line_number):
                    print("Product deletion successful.\n")
            else: 
                print("Error: Data must be loaded first.\n")

        elif user_option == 6: # Search
            if 'matrix' in locals():
                #search_attribute = 'foo'
                #value = 'bar'
                #matrix.search(search_attribute, value)
                pass
            else: 
                print("Error: Data must be loaded first.\n")

        elif user_option == 7: # Sort
            if 'matrix' in locals():
                #matrix.sort()
                pass
            else: 
                print("Error: Data must be loaded first.\n")

        else: 
            print("Error: Invalid input.\n")


if __name__=='__main__': 
    main()