def swap_case(s):
    new_s = ''

    for i in s:
        
        if (i.isupper()) == True:
            new_s+=i.lower()

        elif (i.isspace()) == True:
            new_s+=i
        
        elif (i.isdigit()) == True:
            new_s+=i

        elif (i.islower()) == True:
            new_s+=i.upper()
        
        else :
            new_s+=i

    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
