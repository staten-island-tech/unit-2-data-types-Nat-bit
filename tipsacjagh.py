#Challenge 5
##Create a function that accepts an input and determines all factors of the number.
#first take inputs
#Second somehow make a list that has the factors of such number in it. 
#Third make a filter for that list to only print out the largest/highest/greatest factors?

num=int(input("number: "))
def factor (x):
    print ("Factors of " ,x," : ")
    for i in range (1, x+1):
        if x % i ==0 :
            print (i)
factor(num)


