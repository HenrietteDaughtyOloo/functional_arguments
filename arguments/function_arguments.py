#A function named concatenate_args that takes any number of string 
#arguments in positional arguments format and concatenates them into
# a single string
def concatenate_args(*string_arguments):
    concatenated = ""
    for string in string_arguments:
        concatenated += string
    return concatenated

#A function named concatenate_kwargs that takes any number of string 
# arguments in keyword arguments  format and concatenates them into 
# a single string

def concatenate_kwargs(**kwargs):
    concatenated = ""
    for key,value in kwargs.items():
        concatenated += value
    return concatenated
    
