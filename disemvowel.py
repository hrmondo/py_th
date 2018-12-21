def disemvowel(word):
    vow = "aeiouAEIOU"
    vow_list = list(vow)
    word_list = list(word)
    
    for char in vow_list:
        try:
            	word_list.remove(char) 
        except ValueError:
        		pass
    
    word =  ''.join(word_list)
    return word
