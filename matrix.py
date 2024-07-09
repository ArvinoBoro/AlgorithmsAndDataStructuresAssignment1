import time 
class Matrix:
    
    def __init__(self, file_name):
        try:
            file_proxy = open(file_name, 'r+')
        except: 
            print("\nError: File not found.\n")
            return None
        
        self._data_raw = file_proxy.read()
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

        print("Data load successful.")

    def __str__(self):
        entries = ""
        for i in range(len(self._data_organized)):
            entries += f"{i+1}. "
            for j in range(4):
                entries += f" {self._data_organized[i][j]}"
                if j < 3:
                    entries += ','
            if i < len(self._data_organized) - 1:
                entries += '\n'

        return entries
    
    def insert(self, position, *argv):

        if not isinstance(position, int):
            print("Error: The line number is not an integer.\n")
            return None
        
        if not len(argv) == len(self._data_organized[0]):
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
    
    def search(self, i, value):
        results = []
        
        if i == 0: 
            for k in range(len(self._data_organized[0])):
                for l in range(len(self._data_organized)):
                    if value == self._data_organized[l][k]:
                        results.append(l + 1)
        else: 
            for j in range(len(self._data_organized)):
                if value == self._data_organized[j][i - 1]: 
                    results.append(j + 1)        
        return results

    def bubble_sort(self, k, sort_in_ascending_order):
        start = time.time()

        for i in range(1, len(self._data_organized)):
            for j in range(len(self._data_organized) - i):
                if sort_in_ascending_order and self._data_organized[j][k] > self._data_organized[j+1][k]:
                    temp = self._data_organized[j+1] 
                    self._data_organized[j+1] = self._data_organized[j]
                    self._data_organized[j] = temp
                elif not sort_in_ascending_order and self._data_organized[j][k] < self._data_organized[j+1][k]:
                    temp = self._data_organized[j+1] 
                    self._data_organized[j+1] = self._data_organized[j]
                    self._data_organized[j] = temp
        end = time.time()
        print(f"Sorting algorithm runtime: {end - start} s")

        return 1
        
    def get_number_of_columns(self):
        return len(self._data_organized[0])
    
    def get_number_of_rows(self):
        return len(self._data_organized)
                    