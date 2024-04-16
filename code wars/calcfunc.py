def zero(a=None): 
    if a:
        return eval('0'+a)
    else:
        return '0'
def one(a=None): 
    if a:
        return eval('1'+a)
    else:
        return '1'
def two(a=None): 
    if a:
        return eval('2'+a)
    else:
        return '2'
def three(a=None): 
    if a:
        return eval('3'+a)
    else:
        return '3'
def four(a=None):  
    if a:
        return eval('4'+a)
    else:
        return '4'
def five(a=None): 
    if a:
        return eval('5'+a)
    else:
        return '5'
def six(a=None):  
    if a:
        return eval('6'+a)
    else:
        return '6'
def seven(a=None): 
    if a:
        return eval('7'+a)
    else:
        return '7'
def eight(a=None): 
    if a:
        return eval('8'+a)
    else:
        return '8'
def nine(a=None): 
    if a:
        return eval('9'+a)
    else:
        return '9'
 
def plus(a): return '+'+a
def minus(a): return '-'+a
def times(a): return '*'+a
def divided_by(a): return '/'+a
 
print(seven(times(five())))