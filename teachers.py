# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers (course_dic):
	#course_dic = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}
    
    num_teacher = len(course_dic)
    
    return num_teacher

def num_courses(course_dic):
    	
    course_list = []
    for v in course_dic.values():
        course_list += v
        
    return len(course_list)


def courses(course_dic):
    	
    course_list = []
    for v in course_dic.values():
        course_list += v
        
    return course_list

def most_courses(course_dic):
    
    teacher_max = 0
    great_teacher= " "
    for teacher, course in course_dic.items():
        if len(course) > teacher_max:
            teacher_max = len(course)
            great_teacher = teacher
            
    return  great_teacher



def stats(course_dic):

    stats_list = []

    for teacher, course in course_dic.items():

        stats_list.append([teacher, len(course)])

    return stats_list