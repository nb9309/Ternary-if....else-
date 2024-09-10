a= float(input("enter value1: "))
b = float(input("enter value2: "))
if a > b:
    bv = a
elif b > a:
    bv = b
else:
    bv = 'both are equal'

print('max(%0.2f, %0.2f) = %s' %(a,b,bv))
