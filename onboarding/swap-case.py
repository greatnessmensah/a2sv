def swap_case(s):
    t = ""
    
    for i in s:
        if i.islower():
            i = i.upper()
            t += i
        elif i.isupper():
            i = i.lower()
            t += i
        else:
            t += i
            
    return t
        
    

if __name__ == '__main__':
