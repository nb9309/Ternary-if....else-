
a,b=float(input("Enter Value of a:")),float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
#code for finding big
#res=a if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "All values are equal"
# OR---the above can be written as Follows
res=a if(b<=a>c) else b if(a<b>=c) else c if (a<=c>b) else "All values are equal"
print("Max({},{},{})={}".format(a,b,c,res))


