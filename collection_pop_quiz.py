
messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
# Your code goes below here
my_item = messy_list.pop(3)
messy_list.insert(0, my_item)

num_list = []
for item in messy_list:
        if type(item) == int: 
        	num_list.append(item) 
        
del messy_list[0:6]
messy_list = num_list