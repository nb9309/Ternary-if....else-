a= float(input("enter value1: "))
b = float(input("enter value2: "))
bv = a if (a>b) else b if a<b else 'both are same'

print('max(%0.2f, %0.2f) = %s' %(a,b,bv))
