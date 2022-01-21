def read_file(filename):
    ''' Read file with filename
        Read one line of student information and return a list of string.

    :param filename: str
    :return: a list of string
    '''
    lines = open(filename).read().splitlines()
    table = [x.split(",") for x in lines if x != ""]
    return table

def extract_name_lists(table):
    ''' Receive nested list of string
            Return the first two columns of string as two separate lists, but exclude the first row

        :param table: nested_list of str
        :return: two lists of str
        >>> extract_name_lists([['FirstName', 'Lastname', 'Grade'],['Ann', 'Smith', 'B+'],['Barry', 'Williams', 'C+']])
        (['Ann', 'Barry'], ['Smith', 'Williams'])
        >>> extract_name_lists([['FirstName', 'Lastname'],['Cathy', 'Johnson'],['David', 'Jones'],['Eric', 'Garcia']])
        (['Cathy', 'David', 'Eric'], ['Johnson', 'Jones', 'Garcia'])
        >>> extract_name_lists([['FirstName', 'Lastname', '101', '102'],['Irene', 'Wilson', 'B', 'B+']])
        (['Irene'], ['Wilson'])
        '''
    firstname_list = []
    lastname_list = []
    for i in range(1,len(table)):
        firstname_list.append(table[i][0])
        lastname_list.append(table[i][1])
    return firstname_list, lastname_list

def extract_course_list(table):
    ''' Receive nested list of string
            Return the first row (course names), but not the first two members (first name and last name)

        :param table: nested_list of str
        :return: a list of str
        >>> extract_course_list([['FirstName', 'Lastname', '01219114'],['Ann', 'Smith', 'B+'],['Barry', 'Williams', 'C+']])
        ['01219114']
        >>> extract_course_list([['FirstName', 'Lastname', '101', '102'],['Irene', 'Wilson', 'B', 'B+']])
        ['101', '102']
        >>> extract_course_list([['FirstName', 'Lastname'],['Cathy', 'Johnson'],['David', 'Jones'],['Eric', 'Garcia']])
        []
        '''
    list1 = []
    for i in range(2,len(table[0])): #table 0 เพราะไล่ในช่อง 0
        list1.append(table[0][i])
    return list1

def convert_one_grade_point(grade):
    ''' Receive one letter grade and return a point grade.

        :param grade: str
        :return: float
        >>> convert_one_grade_point('A')
        4.0
        >>> convert_one_grade_point('D+')
        1.5
        >>> convert_one_grade_point('F')
        0.0
        '''
    if grade == "A":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1.0
    else:
        return 0.0

def convert_all_grade_points(grade_str_table):
    ''' Receive nested list of letter grades and convert to point grades
            Return

        :param grade_str_table: nested_list of str
        :return: nested_list of float
        >>> convert_all_grade_points([['A','B'], ['B+','C']])
        [[4.0, 3.0], [3.5, 2.0]]
        >>> convert_all_grade_points([['D+','D','C+']])
        [[1.5, 1.0, 2.5]]
        >>> convert_all_grade_points([['F'], ['A'], ['B+']])
        [[0.0], [4.0], [3.5]]
        '''
    list1 = []
    for i in range(len(grade_str_table)):
        list2 = []
        for j in range(len(grade_str_table[i])):
            list2.append(convert_one_grade_point(grade_str_table[i][j]))
        list1.append(list2)
    return list1

def get_grade_point_table(table):
    ''' Receive nested list of string containing letter grades of all students, all courses
            Return nested list of float containing point grades of all students, all courses

        :param table: nested list of str
        :return: nested list of float
        >>> get_grade_point_table([['FirstName', 'Lastname', '01219114'],['Ann', 'Smith', 'B+'],['Barry', 'Williams', 'C+']])
        [[3.5], [2.5]]
        >>> get_grade_point_table([['FirstName', 'Lastname', '101', '102'],['Irene', 'Wilson', 'B', 'B+']])
        [[3.0, 3.5]]
        >>> get_grade_point_table([['FirstName', 'Lastname'],['Cathy', 'Johnson'],['David', 'Jones'],['Eric', 'Garcia']])
        [[], [], []]
        '''
    list1 = []
    for i in range(1, len(table)):
        list2 = []
        for j in range(2, len(table[i])):
             list2.append(table[i][j])
        list1.append(list2)
    return convert_all_grade_points(list1)

def compute_ave_student_grade(grade_point_table):
    ''' Receive nested list of float, containing point grades of all students, all courses
            Return the list of average grade for each student

        :param grade_point_table: nested list of float
        :return: a list of float
        >>> compute_ave_student_grade([[0.0, 0.0, 0.0], [4.0, 3.5, 1.5]])
        [0.0, 3.0]
        >>> compute_ave_student_grade([[2.0, 1.0], [4.0, 1.5], [2.0, 1.0]])
        [1.5, 2.75, 1.5]
        >>> compute_ave_student_grade([[1.0], [0.0], [4.0], [2.5]])
        [1.0, 0.0, 4.0, 2.5]
        '''
    list1 = []
    for i in range(len(grade_point_table)):
        list1.append(sum(grade_point_table[i])/len(grade_point_table[i]))
    return list1

def compute_ave_course_grade(grade_point_table):
    ''' Receive nested list of float, containing point grades of all students, all courses
            Return the list of average grade for each course

        :param grade_point_table: nested list of float
        :return: compute_ave_course_grade
        >>> compute_ave_course_grade([[0.0, 0.0, 0.0], [4.0, 3.5, 1.5]])
        [2.0, 1.75, 0.75]
        >>> compute_ave_course_grade([[2.0, 1.0], [4.0, 1.5], [2.0, 1.0]])
        [2.6666666666666665, 1.1666666666666667]
        >>> compute_ave_course_grade([[1.0], [0.0], [4.0], [2.5]])
        [1.875]
        '''
    list1 = []
    for i in range(len(grade_point_table[0])):
        s = 0
        for j in range(len(grade_point_table)):
            s += grade_point_table[j][i]
        list1.append(s/len(grade_point_table))
    return list1

def find_item_list(
                   item_list,
                   search_str):
    ''' Receive a list of items (item_list) and string to be searched (search_str)
            Return a list containing indexes of string that matche the search_str

        :param item_list: a list of str
        :param search_item: str
        :return: a list of int
        >>> find_item_list(['Ann', 'Barry', 'Cathy'], 'Ann')
        [0]
        >>> find_item_list(['Ann', 'Barry', 'Ann', 'Cathy'], 'Ann')
        [0, 2]
        >>> find_item_list(['Ann', 'Barry', 'Cathy'], 'David')
        []
        >>> find_item_list(['01420111', '01219114', '01355112', '01417167'], '01219114')
        [1]
        '''
    list1 = []
    for i in range(len(item_list)):
        if item_list[i] == search_str:
            list1.append(i)
    return list1

def get_column_list(
                    nested_list,
                    index):
    ''' Receive nested list of numbers and a column index
            Return a list of numbers from the column with the given column index

        :param nested_list: nested list of floats
        :param index: int
        :return: a list of float
        >>> get_column_list([[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]], 2)
        [3, 8, 13]
        >>> get_column_list([[13, 15, 17], [28, 26, 24]], 1)
        [15, 26]
        >>> get_column_list([[6, 12, 18]], 0)
        [6]
        '''
    list1 = []
    for i in range(len(nested_list)):
        list1.append(nested_list[i][index])
    return list1

def find_below_index_list(
                          item_list,
                          threshold):
    ''' Receive a list of numbers (item_list) and a threshold value
            Return a list of indexes corresponding to numbers that are less than the threshold
        :param item_list: a list of floats
        :param threshold: float
        :return: a list of int
        >>> find_below_index_list([4.0, 3.5, 2.0, 1.5], 2.0)
        [3]
        >>> find_below_index_list([28, 26, 24], 27.0)
        [1, 2]
        >>> find_below_index_list([6, 12, 18], 5.0)
        []
        '''
    list1 = []
    for i in range(len(item_list)):
        if item_list[i] < threshold:
            list1.append(i)
    return list1

def print_partial_students(
                           firstname_list,
                           lastname_list,
                           course_list,
                           grade_point_table,
                           index_list):
    ''' Receive a list of first names, last names, course numbers, and grade point table.
            Also receive a list of row indexes.
            Show student information from the given rows
        :param firstname_list: a list of strings
        :param lastname_list: a list of strings
        :param course_list: a list of strings
        :param grade_point_table: nested list of floats
        :param index_list: a list of int
        '''
    print('                     : ', end='')
    for j in range(len(course_list)):
        print(f'{course_list[j]:8}', end=' ')
    print()
    for i in range(len(index_list)):
        print(f'{firstname_list[index_list[i]]:10} {lastname_list[index_list[i]]:10}: ', end='')
        for j in range(len(course_list)):
            print(f'{grade_point_table[index_list[i]][j]:8}', end=' ')
        print()

def operate(
            firstname_list,
            lastname_list,
            course_list,
            grade_point_table,
            choice):
    ''' Receive a list of first names, last names, course numbers, and grade point table.
            Also receive user's choice as int.
            Perform action corresponding to the choice

        :param firstname_list: a list of strings
        :param lastname_list: a list of strings
        :param course_list: a list of strings
        :param grade_point_table: nested list of floats
        :param choice: int
        '''
    if choice == 1:
        for i in range(len(grade_point_table)):
            print(f"{firstname_list[i]} {lastname_list[i]} : {compute_ave_student_grade(grade_point_table)[i]:.2f}")
    elif choice == 2:
        for i in range(len(course_list)):
            print(f"{extract_course_list(table)[i]} : {compute_ave_course_grade(grade_point_table)[i]:.2f}")
    elif choice == 3:
        search_str = str(input("Enter name to search: "))
        index_list = find_item_list(firstname_list,
                                    search_str)
        print_partial_students(firstname_list,
                               lastname_list,
                               course_list,
                               grade_point_table,
                               index_list)
    else:
        search_str = str(input("Enter course to search: "))
        threshold = float(input("Enter threshold: "))
        index_course = find_item_list(course_list,
                                      search_str)
        item_list = get_column_list(grade_point_table,
                                    index_course[0])
        index_list = find_below_index_list(item_list,
                                           threshold)
        print_partial_students(firstname_list,
                               lastname_list,
                               course_list,
                               grade_point_table,
                               index_list)



filename = "students_small.txt"    # or "students_large.txt"
table = read_file(filename)
#print(table)                  # Uncomment this line to see what table looks like

firstname_list, lastname_list = extract_name_lists(table)
course_list = extract_course_list(table)
grade_point_table = get_grade_point_table(table)
print('1. Compute average student grades')
print('2. Compute average course grades')
print('3. Find grades by first name')
print('4. Find students with below grade')
choice = int(input('Enter choice: '))
operate(firstname_list,
        lastname_list,
        course_list,
        grade_point_table,
        choice)


if __name__ == "__main__":
    import doctest
    doctest.testmod()




