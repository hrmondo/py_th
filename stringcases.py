def stringcases(string):
    
    final = ()
    string_upper = string.upper()
    string_lower = string.lower()
    string_title = string.title()
    string_reverse = string[::-1]
    
    final = (string_upper, string_lower, string_title, string_reverse)
   
    return final

##why capilitaze() and reverse() are not allowed??