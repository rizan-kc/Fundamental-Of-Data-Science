'''
The program takes the list of names and sort them in ascending alphabetical order
'''
def sort_name(lst):
    '''
    Sorts a list of names in alphabetical order.
    Parameters:
    lst: A list of names

    Returns the alphabetically sorted list.
    '''
    lst.sort()
    return lst
name = ["Rizan","Ram","Radha","Prashish","Younesh"]
print("Before sorting the name list:\n",name)
sorted_list = sort_name(name)
print("After sorting the name list:\n",sorted_list)