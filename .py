#challenge 6
#Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.

num= int(input("1st number? "))
num2= int(input("2nd number? "))

def gcf(x,y):
    while y:
        x,y= y,x % y
        return x
    
print (f"The greatest common factor of {num} and {num2} is " + str(gcf(num,num2)))

