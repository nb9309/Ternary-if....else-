a= float(input("enter value1: "))
b = float(input("enter value2: "))
c = float(input("enter value2: "))
if (a>=b) and (a>c):
    #(c<a>=b)
    res = a
elif (b>a)and(b>=c):
    #(c<=b>a)
    res = b
elif (c>=a)and (c>b):
    #(b<c>=a)
    res = c
else:
    res = 'same'

print('max(%0.2f, %0.2f, %0.2f) = %s' %(a,b,c,res) )
