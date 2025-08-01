class ArrayList:
    def __init__(self):
        self.memory =[None for i in range(2)] # remember anything self. will become an instance of the class or method
        self.arr_length = 0

    def increase_array_size(self):
            # Grabbing new portion of memory
            new_memory = [None for i in range(len(self.memory) * 2)] # doubles the memory
            # Copy over old array into memory
            for index, copy in enumerate(self.memory):
                new_memory[index] = copy
            self.memory = new_memory 


    def append(self, elem):
        if self.arr_length >= len(self.memory):
            self.increase_array_size()


        self.memory[self.arr_length] = elem
        self.arr_length += 1


    def get(self, index):
        if index >= self.arr_length:
            raise Exception("index out of bounds!")
        return self.memory[index]


    def remove(self,elem):
        """
        elem = B
        Removes first element that matches our element
        """
        # True if we removed the elem, false otherwise
        index_of_elem = -1
        for index, arry_elem in enumerate(self.memory):
            if arry_elem == elem:
                index_of_elem = index
                break

        if index_of_elem == -1:
            return False

        for i in range(index_of_elem, self.arr_length - 1):
            self.memory[i] = self.memory[i + 1]

        self.memory[self.arr_length] = None
        self.arr_length -= 1
        return True


    def insert(self, index, elem):
        if self.arr_length >= len(self.memory):
            self.increase_array_size()
        self.memory[index] = elem

        for i in range(self.arr_length, index, -1): # starts from the end of the array (self.arr_length) to the end of the index (index) moving left (-1)
            self.memory[i] = self.memory[i - 1] 
            
    def min(self):
        min_element = float("inf") # initalizes positive inifinity
        for index in range(self.arr_length):
            if self.memory[index] < min_element:
                min_element = self.memory[index]
        return min_element
    
    def max(self):
        max_element = float("-inf") # initalizes negative inifinity
        for index in range(self.arr_length):
            if self.memory[index] > max_element:
                max_element = self.memory[index]
        return max_element
    
    def slice(self,start,end):
        start = max(start, 0)
        end = min(end, self.arr_length)
        tmp_arr =[]
        for index in range(start,end):
            tmp_arr.append(self.memory[index])
        return tmp_arr








    def __str__(self):
        return f"{self.memory}"
    

arr = ArrayList()
print(arr)
arr.append(4)
arr.append(3)
arr.append(2)
arr.append(1)
print(arr.slice(0,3))


# list comprehension
# define an array using an expression
print([i for i in range(6)])
dim = 5
square = [[None for col in range(dim)]for row in range(dim)]
for elem in square:
    print(elem)


# vs
print([0,1,2,3,4,5])


