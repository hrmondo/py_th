COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(p):
    
    result = []
    
    for key, value in COURSES.items():
    
        #set intersection
        if p & value:
            result.append(key)
    
    return result


def covers_all(q):

    output = []
    deduct_list= []

    a = set(output)
    b = set(deduct_list) 

    for k, v in COURSES.items():

        #set intersection
        if q & v:
            if k not in output:
            output.append(k)
        else:
            deduct_list.append(k)
 
    #output.difference(deduct_list)

    a.difference(b)


    return a
    

#passed

def covers_all(q):

    output = []
    for k, v in COURSES.items():
        #Test whether every element in the set is in other.
        if q <= v:
            if v not in output:
                output.append(k)
    return output



#failed to pass

def covers_all(q):

    output = []
    deduct_list= []

    for k, v in COURSES.items():

        #set intersection
        if q & v:
            if v not in output:
                output.append(k)
        elif:
            if v not in output:
            deduct_list.append(k)
            
    output.difference(deduct_list)

    return output

    


## Copy from the Internet

    def covers_all(topics):
    new_list = []
    temp_list = []
    for basics in COURSES:
        for topic in topics:
            if topic in COURSES[basics]:              
                temp_list.append(topic)
        if len(topics) == len(temp_list):
            if basics not in new_list:
                new_list.append(basics)
                temp_list = []
        else:
            temp_list = []
    return new_list