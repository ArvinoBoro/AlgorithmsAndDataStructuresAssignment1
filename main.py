class Matrix:
    
    def __init__(self, file_name):
        try:
            fp = open(file_name, 'r+')
        except: 
            print("\nError: File not found.\n")
            return None
        
        self._product_data_raw = fp.read()
        self._product_data_organized = []
        entry = []
        datum = str()
        
        for i in range(len(self._product_data_raw)):
                if self._product_data_raw[i] == '\n':
                    entry.append(datum)
                    self._product_data_organized.append(entry)
                    entry = []
                    datum = ""
                elif self._product_data_raw[i] == ',' and self._product_data_raw[i+1] == ' ':
                    i += 1
                    entry.append(datum)
                    datum = ""
                else:
                    datum += self._product_data_raw[i]

        if datum:
            entry.append(datum)
            self._product_data_organized.append(entry)

        print("\nData load successful.\n")

    def __str__(self):
        entry = ""
        entries = ""
        j = 1
        for i in range(len(self._product_data_raw)):
            if self._product_data_raw[i] == '\n':
                entries += f"{j}. {entry}\n"
                entry = ""
                j += 1 
            else:
                entry += self._product_data_raw[i]

        return entries 
                           
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

        elif user_option == 2:
            if 'matrix' in locals():
                print(f"\n{matrix}")
            else:
                print("\nError: Data must be loaded first\n")

        elif user_option == 3: # Insert 
            if 'matrix' in locals():
                #position = int(input("Position: "))
                #matrix.insert(position)
                pass

        elif user_option == 4: # Update 
            if 'matrix' in locals():
                #line_number = int(input("Line number: "))
                #matrix.update(line_number)
                pass
            else: 
                print("Error: Data must be loaded first")

        elif user_option == 5: # Delete 
            if 'matrix' in locals():
                #line_number = int(input("Line number: "))
                #matrix.delete(line_number)
                pass
            else: 
                print("Error: Data must be loaded first")

        elif user_option == 6: # Search
            if 'matrix' in locals():
                #search_attribute = 'foo'
                #value = 'bar'
                #matrix.search(search_attribute, value)
                pass
            else: 
                print("Error: Data must be loaded first")

        elif user_option == 7: # Search
            if 'matrix' in locals():
                #matrix.sort()
                pass
            else: 
                print("\nError: Data must be loaded first\n")

        else: 
            print("\nError: Invalid input\n")


if __name__=='__main__': 
    main()