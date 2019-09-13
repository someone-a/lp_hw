def two_string_function(str1, str2):
    if not(type(str1) == str and type(str2) == str): 
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) >= len(str2):
        return 2
    elif str2 == 'learn':
        return 3
    else:
        print('another case')