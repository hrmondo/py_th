def first_4(whatever_item):
    
    four_item = whatever_item[0:4]
    
    return four_item

def first_and_last_4(whatever_item):
    
    first_4item = whatever_item[:4]
    
    last_4item= whatever_item[-4:]
    
    first_last_four = first_4item + last_4item
    
    return first_last_four

def odds(whatever_item):
    
    odd_item = whatever_item[1::2]
    
    return odd_item

def reverse_evens(whatever_item):
    
    even_item = whatever_item[0::2]

    reverse_even = even_item[::-1]   

    return reverse_even        

