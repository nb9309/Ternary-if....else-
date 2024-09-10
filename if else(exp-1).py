value =(input('enter value: '))
if value == value[::-1]:
    #value[::]==value[::-1]
    #value[::1] == value[::-1]
    res = 'palendrome'
else:
    res = 'not a palendrome'
print("{} is {}".format(value,res))