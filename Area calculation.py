print("Enter a to calculate area of a square.")
print("Enter b to caluclate area of a rectangle.")
print("Enter c to calculate area of a triangle.")
ch= input("Enter you choice: ")
if (ch=='a'):
	s=int(input("Enter side."))
	ars=s**2
	print("Area of the square is: ",ars)
elif (ch=='b'):
	l=int(input("Enter length of the rectangle."))
	b=int(input("Enter breadth of the reactangle."))
	ar=l*b
	print("Area of the reactangle is: ",ar)
elif(ch=='c'):
	a=int(input("Enter the length if first side of the triangle."))
	b=int(input("Enter the length if second side of the triangle."))
	c=int(input("Enter the length if third side of the triangle."))
	s=(a+b+c)/2
	at=(s*(s-a)*(s-b)*(s-c))**0.5
	print("Area of the triangle is: ",at)
else:
	print("Wrong input. Please enter the correct option.")
	
	
