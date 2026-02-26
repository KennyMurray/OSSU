#Lecture 13 finger exercise

def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    Lnew = ""
    
    for i in L:
        if type(i) == list:
            for j in i:
                if type(j) != str:
                    raise ValueError("List elements are not all strings")
                Lnew += j
        elif type(i) == str:
            Lnew += i
        else:
            raise ValueError("None string character")
    return len(Lnew)
            

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError