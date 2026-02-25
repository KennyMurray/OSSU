#Lecture 10 finger exercise

def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    for f in Lf:
        if f(n) == False:
            return False
    return True
# Examples:    
all_true() # prints 6