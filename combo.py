# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]



def combo(ite1, ite2):
    
    #1 prepare a list to return
    result = []

    #2 position
    n = 0

    #3 for statement 
    for item1 in ite1:
        item2 = ite2[n]
        n_list = (item1, item2)
        #4 .append()
        result.append(n_list)
        #5 position increment
        n += 1
    
    return result

  #zip
  #def combo(iter1, iter2):
  #return list(zip(iter1, iter2))