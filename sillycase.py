
def sillycase(c): 
  return c[:round(len(c) / 2)].lower() + c[round(len(c) / 2):].upper()



#slice_list = []
#def sillycase(original_string):
#	
#    slice_list[] = original_string
#    
#    half_point = int(len(slice_list)/2)
#
#    first_half = original_string[:half_point+1]
#    first_half.lower()
#
#    last_half = original_string[half_point:]
#    last_half.upper()
#
#    total = first_half + last_half
#
#    sillystring = ["".join.total]
#    return sillystring 
#
#
    # lower(). upper()



# lower(), upper() は関数調べればよいとして、
# なんかえらい迷走したので記録しておきたい。
#文字列を一度分割して処理してからつなぎ合わせるのかと思って書いていた。。




I need you to create a new function for me.

This one will be named sillycase and it'll take a single string as an argument.

sillycase should return the same string but the first half should be lowercased and the second half should be uppercased. For example, with the string \"Treehouse\", sillycase would return \"treeHOUSE\".

Don't worry about rounding your halves, but remember that indexes should be integers. You'll want to use the int() function or integer division, //."



